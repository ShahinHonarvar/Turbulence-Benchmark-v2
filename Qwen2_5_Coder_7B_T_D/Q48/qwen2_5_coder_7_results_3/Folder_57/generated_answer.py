def return_binary_or_hexa(numbers):
    a, b = (numbers[25], numbers[80])
    total = sum(range(a + 1, b))
    missing_numbers = [num for num in range(a + 1, b) if num not in numbers[a + 1:b]]
    if missing_numbers:
        total = sum(missing_numbers)
    return bin(total)[2:] if total % 2 != 0 else hex(total)[2:].upper()