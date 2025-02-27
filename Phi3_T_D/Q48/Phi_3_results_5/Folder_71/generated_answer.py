def return_binary_or_hexa(numbers):
    a, b = (numbers[20], numbers[35])
    non_present = [i for i in range(a + 1, b) if i not in numbers[20:36]]
    if non_present:
        total_sum = sum(non_present)
        if total_sum % 2:
            return bin(total_sum)[2:]
        else:
            return hex(total_sum)[2:]
    return ''