def return_binary_or_hexa(t):
    a, b = (t[22], t[24])
    total_sum = sum(range(a + 1, b))
    missing = [i for i in range(a + 1, b) if i not in t[22:25]]
    total_sum += sum(missing)
    if total_sum % 2 == 0:
        return format(total_sum, 'x')
    else:
        return format(total_sum, 'b')