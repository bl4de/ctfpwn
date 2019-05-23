#!/usr/bin/env python
import unittest
import ctfpwn

test_url = 'https://google.ie'

hs = '5374657068616e69652052616f'
b64s = 'U3RlcGhhbmllIFJhbw=='
ps = 'Stephanie Rao'

class CtfpwnTestSuite(unittest.TestCase):
    def test_to_base64(self):
        self.assertEqual(ctfpwn.to_base64(ps),b64s)

    def test_from_base64(self):
        self.assertEqual(ctfpwn.from_base64(b64s),ps)

    def test_md5(self):
        self.assertEqual(ctfpwn.md5('admin'),
                         '21232f297a57a5a743894a0e4a801fc3')

    def test_find_in_response(self):
        resp = ctfpwn.http_get(test_url)
        self.assertTrue(ctfpwn.find_in_response(resp, 'Google'))
        self.assertFalse(ctfpwn.find_in_response(resp, 'XYZXYZ'))

    def test_http_headers(self):
        self.assertEqual(ctfpwn.http_headers(test_url, 'Content-Encoding'),
                         'gzip')

    def test_split_string(self):
        self.assertEqual(ctfpwn.split_string('AAAAAA', 2), 'AA AA AA')
        self.assertEqual(ctfpwn.split_string('1001001110010101', 4), '1001 0011 1001 0101')

    def test_hex_to_ascii(self):
        self.assertEqual(ctfpwn.hex_to_ascii(hs), ps)
        self.assertEqual(''.join(ctfpwn.ascii_to_hex(ps)), hs)

if __name__ == '__main__':
    print("\nctfpwn Test Suite\n\n")
    unittest.main()
