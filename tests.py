#!/usr/bin/env python
import ctfpwn

s = '496e73696768747320617320696e636964656e7420726573706f6e64657273206f6e20427573696e65737320456d61696c20436f6d70726f6d69736573'
a = ctfpwn.hex_to_ascii(s)
print a

s = 'Stephanie Rao'
h = ''.join(ctfpwn.ascii_to_hex(s))
print h

print h == s