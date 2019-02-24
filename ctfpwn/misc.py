# ctfpwn/misc - misc routines do do misc stuff :)


def split_string(__string, __chunk_length):
    """
    splits string into __chunk_length len chunks
    
    >>> import ctfpwn
    >>> s = "57702A6C58744751386538716E6D4D59552A737646486B6A49742A52"
    >>> print ctfpwn.split_string(s, 2)
    57 70 2A 6C 58 74 47 51 38 65 38 71 6E 6D 4D 59 55 2A 73 76 46 48 6B 6A 49 74 2A 52
    >>> print ctfpwn.split_string(s, 8)
    57702A6C 58744751 38653871 6E6D4D59 552A7376 46486B6A 49742A52

    """
    str_pos = 0
    chunked = ""
    while len(__string) > str_pos:
        chunked = chunked + __string[str_pos:str_pos+__chunk_length] + " "
        str_pos = str_pos + __chunk_length

    return chunked
