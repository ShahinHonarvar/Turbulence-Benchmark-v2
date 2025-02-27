def return_binary_or_hexa(tu):
    if not 56 <= b <= 88 <= len(tu):
        return ''
    s = sum(set(range(tu[56] + 1, tu[88])) - set(tu[56:88]))
    return bin(s)[2:] if s % 2 else ('{:X}' if s % 16 == 0 else '{:x}').format(s)