import binhex

def return_binary_or_hexa(tup):
    a, b = (tup[32], tup[99])
    sum_val = sum(range(a + 1, b))
    missing_ints = set(range(a + 1, b)) - set(tup[32:100])
    sum_val -= sum(missing_ints)
    if sum_val % 2 == 1:
        return binhex.bin(sum_val)[2:]
    else:
        return binhex.hex(sum_val)[2:]