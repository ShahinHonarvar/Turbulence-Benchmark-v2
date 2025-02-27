def return_binary_or_hexa(numbers):
    a, b = (numbers[0], numbers[-1])
    absent = [x for x in range(a + 1, b) if x not in numbers]
    total = sum(absent)
    if total % 2 != 0:
        return bin(total)[2:]
    else:
        return hex(total)[2:]