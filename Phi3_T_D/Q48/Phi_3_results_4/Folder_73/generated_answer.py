def return_binary_or_hexa(numbers):
    a, b = (numbers[10], numbers[76])
    diff_sum = sum((x for x in range(a + 1, b) if x not in numbers[10:77]))
    return bin(diff_sum)[2:] if diff_sum % 2 else hex(diff_sum)[2:]