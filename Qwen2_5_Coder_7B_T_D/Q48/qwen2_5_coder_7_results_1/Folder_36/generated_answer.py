def return_binary_or_hexa(numbers):
    a, b = (numbers[110], numbers[348])
    missing_sum = sum(range(a + 1, b)) - sum(set((numbers[i] for i in range(110, 349))))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:].upper()