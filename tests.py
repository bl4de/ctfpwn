#!/usr/bin/env python
import ctfpwn

print(ctfpwn.to_base64('Audi A4'))

print(ctfpwn.pickle_expolit_generator("os.system('ls -l')"))