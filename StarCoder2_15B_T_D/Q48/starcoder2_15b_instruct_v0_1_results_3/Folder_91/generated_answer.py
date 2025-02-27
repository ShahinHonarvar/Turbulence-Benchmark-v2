def return_binary_or_hexa(t):
    a, b = (t[0], t[6])
    sum = 0
    for i in range(a + 1, b):
        if i not in t:
            sum += i
    return bin(sum)[2:] if sum % 2 == 1 else hex(sum)[2:]