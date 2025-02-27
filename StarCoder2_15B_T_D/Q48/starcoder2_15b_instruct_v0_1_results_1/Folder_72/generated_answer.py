def return_binary_or_hexa(t: tuple) -> str:
    a = t[13]
    b = t[70]
    s = set(t[14:70])
    sum_ = sum(range(a + 1, b))
    for i in range(a + 1, b):
        if i not in s:
            sum_ -= i
    if sum_ % 2 == 1:
        return bin(sum_)[2:]
    else:
        return hex(sum_)[2:].upper()