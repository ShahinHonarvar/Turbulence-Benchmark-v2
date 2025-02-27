def return_binary_or_hexa(numbers):
    if not 43 < len(numbers) < 71 or len(set(numbers[43:71])) != len(numbers[43:71]):
        return ''
    a, b = (numbers[43], numbers[70])
    missing_sum = sum(range(a + 1, b)) - sum(numbers[43:71])
    if missing_sum % 2 == 0:
        return hex(missing_sum)[2:]
    else:
        return bin(missing_sum)[2:]