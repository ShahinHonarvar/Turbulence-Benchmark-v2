def return_binary_or_hexa(t):
    a, b = (t[10], t[76])
    s = set(t[11:76])
    summation = 0
    for i in range(a + 1, b):
        if i not in s:
            summation += i
    if summation == 0:
        return ''
    if summation % 2 == 1:
        return bin(summation)[2:]
    else:
        return hex(summation)[2:]