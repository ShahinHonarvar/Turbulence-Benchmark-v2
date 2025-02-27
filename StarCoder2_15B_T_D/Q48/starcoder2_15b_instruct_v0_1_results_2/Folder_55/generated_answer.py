def return_binary_or_hexa(t):
    a = t[10]
    b = t[12]
    sum_ = 0
    for i in range(a + 1, b):
        if i not in t:
            sum_ += i
    if sum_ % 2 == 1:
        return bin(sum_)[2:]
    else:
        return hex(sum_)[2:].upper()