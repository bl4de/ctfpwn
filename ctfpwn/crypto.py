def rot13(ciphertext, step=13):
    """
    Executes ROT 13 on ciphertext
    It can be called with any ROT value; 13 is by default 
    """
    valid = ""
    for x in range(0, len(ciphertext)):
        # ROT13 only for ASCII codes from 97 to 122 decimal:
        if ord(ciphertext[x]) in range(97, 122):
            if (ord(ciphertext[x]) + step) > 122:
                valid += chr(ord(ciphertext[x]) - step)
            else:
                valid += chr(ord(ciphertext[x]) + step)
        else:
            valid += ciphertext[x]

    return valid
