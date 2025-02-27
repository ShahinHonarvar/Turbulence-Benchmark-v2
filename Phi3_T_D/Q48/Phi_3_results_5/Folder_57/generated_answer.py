def return_binary_or_hexa(integers):
    a, b = (integers[25], integers[80])
    missing_sum = sum(set(range(a + 1, b)) - set(integers[25:80 + 1]))
    return bin(missing_sum)[2:] if missing_sum % 2 else hex(missing_sum)[2:]