"""Verify the booth API-key adapter without connecting to a real Namespace."""
import os
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import unittest
from unittest.mock import AsyncMock, patch
import client


class CloudConnectionTests(unittest.IsolatedAsyncioTestCase):
    async def test_cloud_key_uses_tls_and_requested_namespace(self):
        env = {'TEMPORAL_HOST_URL': 'synthetic.example:7233', 'TEMPORAL_NAMESPACE': 'synthetic.ns',
               'TEMPORAL_API_KEY': 'synthetic-key'}
        with patch.dict(os.environ, env, clear=True), patch.object(client.Client, 'connect', new_callable=AsyncMock) as connect:
            await client.get_client()
            self.assertEqual(connect.call_args.args, ('synthetic.example:7233',))
            self.assertEqual(connect.call_args.kwargs['namespace'], 'synthetic.ns')
            self.assertEqual(connect.call_args.kwargs['api_key'], 'synthetic-key')
            self.assertTrue(connect.call_args.kwargs['tls'])

    async def test_missing_cloud_target_refuses_to_fall_back_to_local(self):
        with patch.dict(os.environ, {'TEMPORAL_API_KEY': 'synthetic-key'}, clear=True), \
             patch.object(client.Client, 'connect', new_callable=AsyncMock) as connect:
            with self.assertRaises(ValueError):
                await client.get_client()
            connect.assert_not_awaited()

    async def test_local_has_no_cloud_auth(self):
        with patch.dict(os.environ, {'TEMPORAL_HOST_URL': '127.0.0.1:7233', 'TEMPORAL_NAMESPACE': 'default'}, clear=True), \
             patch.object(client.Client, 'connect', new_callable=AsyncMock) as connect:
            await client.get_client()
            self.assertEqual(connect.call_args.args, ('127.0.0.1:7233',))
            self.assertNotIn('api_key', connect.call_args.kwargs)
            self.assertNotIn('tls', connect.call_args.kwargs)


if __name__ == '__main__':
    unittest.main()
