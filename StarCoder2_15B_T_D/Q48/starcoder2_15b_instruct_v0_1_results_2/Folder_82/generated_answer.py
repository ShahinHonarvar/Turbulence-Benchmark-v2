def return_binary_or_hexa(t):
    start, end = (t[20], t[200])
    total = 0
    for i in range(start + 1, end):
        if i not in t:
            total += i
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]