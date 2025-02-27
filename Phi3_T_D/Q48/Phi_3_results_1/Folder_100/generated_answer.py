def return_binary_or_hexa(numbers):
    a, b = (numbers[44], numbers[78])
    missing_sum = sum((x for x in range(a + 1, b) if x not in numbers[44:79]))

    def get_representation(i):
        return bin(missing_sum)[2:] if i % 2 else hex(missing_sum)[2:].upper()
    return get_representation(missing_sum)