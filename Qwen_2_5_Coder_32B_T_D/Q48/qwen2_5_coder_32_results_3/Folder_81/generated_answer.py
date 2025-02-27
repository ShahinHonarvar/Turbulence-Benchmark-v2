def return_binary_or_hexa(t):
    a, b = (t[10], t[100])
    s = 0
    j = 11
    for i in range(a + 1, b):
        if j < 100 and t[j] == i:
            j += 1
        else:
            s += i
    if s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:].upper()