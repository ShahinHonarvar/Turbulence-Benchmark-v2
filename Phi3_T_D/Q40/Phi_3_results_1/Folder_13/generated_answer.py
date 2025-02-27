def return_n_smallest_chars(s):
    return sorted([c for c in s if ord(c) <= 31 or c in ' !"#$%&()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_abcdefghijklmnopqrstuvwxyz{|}~'])[:31]