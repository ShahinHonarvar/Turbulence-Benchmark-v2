def return_binary_or_hexa(a):
    a = sorted(a)
    sum = 0
    for i in range(a[36] + 1, a[54]):
        if i not in a:
            sum += i
    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper()