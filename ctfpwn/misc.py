# ctfpwn/misc - misc routines do do misc stuff :)


def get_character_set(lc=False, uc=False, nb=False, sc=False):
    """
    returns string of characters for misc iterations
    lc - lowercase
    uc - uppercase
    nb - numbers
    sc - special characters
    """
    lc_char_set = 'abcdefghijklmnopqrstuwvyxz'
    uc_char_set = 'ABCDEFGHIJKLMNOPQRSTUWVXYZ'
    nb_char_set = '0123456789'
    sc_char_set = '._-()[]{}/\?!@#$%^&*:;\'`|,\\%+='

    char_set = ''

    if lc == True:
        char_set = char_set + lc_char_set
    if uc == True:
        char_set = char_set + uc_char_set
    if nb == True:
        char_set = char_set + nb_char_set
    if sc == True:
        char_set = char_set + sc_char_set

    return char_set


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

    return chunked.strip()


def transform_string_into_array(__string, __array_type):
    """
    transforms strigs into array of predefined values for further processing
    handled __array_type values:
    'binary' - transforms into array of 8-bit chunks like ['10011001',...]
    'ascii' - transforms into array of ASCII codes like ['56', '2B', ...]
    """
    separator = ' '
    if __array_type == 'binary':
        return split_string(__string, 8).split(separator)
    if __array_type == 'ascii':
        return split_string(__string, 2).split(separator)

    # return __string if no __array_type is defined or unknown
    return __string


def hex_to_ascii(__hex):
    """
    translates hex byte values into ASCII string
    """
    return ''.join([chr(int(c, 16)) for c in transform_string_into_array(__hex, 'ascii')])


def ascii_to_hex(__ascii):
    """
    translates ASCII string into an array of hex ASCII codes
    """
    return [hex(ord(c)).replace('0x','') for c in __ascii]
