def return_binary_or_hexa(t):
    a, b = (t[80], t[200])
    s = 0
    i = 81
    for n in range(a + 1, b):
        if i < 200:
            while i < 200 and t[i] < n:
                i += 1
            if i >= 200 or t[i] > n:
                s += n
        else:
            s += n
    if s == 0:
        return ''
    elif s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:]