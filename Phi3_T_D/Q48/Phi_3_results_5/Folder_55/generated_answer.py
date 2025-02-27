def return_binary_or_hexa(numbers):
    a = numbers[10]
    b = numbers[12]
    missing_sum = sum(set(range(a + 1, b)).difference(numbers[10:13]))
    if missing_sum == 0:
        return ''
    return bin(missing_sum)[2:] if missing_sum & 1 else hex(missing_sum)[2:]