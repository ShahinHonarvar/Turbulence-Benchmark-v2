def return_binary_or_hexa(numbers):
    sum_ = sum(range(numbers[427] + 1, numbers[669])) - sum(set(range(numbers[427] + 1, numbers[669])) & set(numbers[427:numbers[669]]))
    if sum_ % 2:
        return bin(sum_)[2:]
    else:
        return hex(sum_)[2:]