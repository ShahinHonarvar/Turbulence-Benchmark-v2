def return_binary_or_hexa(numbers):
    a = numbers[10] + 1
    b = numbers[97]
    sum_diff = sum(set(range(a, b)) - set(numbers[10:97]))
    if sum_diff % 2 == 0:
        return hex(sum_diff)[2:]
    else:
        return bin(sum_diff)[2:]