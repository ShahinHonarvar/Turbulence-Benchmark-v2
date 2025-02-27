def return_binary_or_hexa(tup):
    a = tup[13] if len(tup) > 13 else 0
    b = tup[91] if len(tup) > 91 else 0
    sum_ = sum(set(range(a + 1, b)) - set((tup[i] for i in range(13, 92))))
    return bin(sum_)[2:] if sum_ % 2 else hex(sum_)[2:].upper() if hex(sum_).startswith('0x') else hex(sum_)