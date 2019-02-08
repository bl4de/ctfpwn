#!/usr/bin/env python
import unittest
import ctfpwn


class CtfpwnTestSuite(unittest.TestCase):
    def test_to_base64(self):
        self.assertEqual(ctfpwn.to_base64('Stephanie Rao'),
                         'U3RlcGhhbmllIFJhbw==')

    def test_from_base64(self):
        self.assertEqual(ctfpwn.from_base64('U3RlcGhhbmllIFJhbw=='),
                         'Stephanie Rao')

    def test_md5(self):
        self.assertEqual(ctfpwn.md5('admin'),
                         '21232f297a57a5a743894a0e4a801fc3')


if __name__ == '__main__':
    print("\nctfpwn Test Suite\n\n")
    unittest.main()
