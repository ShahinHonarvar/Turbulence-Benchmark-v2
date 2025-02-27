def return_binary_or_hexa(t):
    a = t[68]
    b = t[99]
    sum_ = 0
    for i in range(a + 1, b):
        if i not in t:
            sum_ += i
    if sum_ % 2 == 1:
        return bin(sum_)[2:]
    elif sum_ % 2 == 0:
        return hex(sum_)[2:].upper()
    else:
        return ''