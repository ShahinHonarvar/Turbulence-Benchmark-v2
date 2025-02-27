def return_binary_or_hexa(numbers):
    a = numbers[36]
    b = numbers[54]
    missing_sum = sum(set(range(a + 1, b)).difference(numbers[36:55]))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]