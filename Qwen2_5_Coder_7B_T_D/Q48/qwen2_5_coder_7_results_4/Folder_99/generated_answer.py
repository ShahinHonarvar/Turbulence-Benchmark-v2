def return_binary_or_hexa(numbers):
    a, b = (sorted(numbers)[427], sorted(numbers)[669])
    total_sum = sum(range(a + 1, b))
    missing_numbers = [i for i in range(a + 1, b) if i not in numbers[427:670]]
    if sum(missing_numbers) % 2 == 1:
        return bin(sum(missing_numbers))[2:]
    else:
        return hex(sum(missing_numbers))[2:].upper()