def return_binary_or_hexa(numbers):
    a, b = (numbers[0], numbers[4])
    total = sum(range(a + 1, b))
    missing = [i for i in range(a + 1, b) if i not in numbers]
    if sum(missing) == 0:
        return ''
    elif sum(missing) % 2 == 1:
        return bin(sum(missing))[2:]
    else:
        return hex(sum(missing))[2:].upper()