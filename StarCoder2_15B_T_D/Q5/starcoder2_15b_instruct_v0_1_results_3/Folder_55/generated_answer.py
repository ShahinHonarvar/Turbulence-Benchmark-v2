def all_neg_ints_inclusive(numbers):
    result = []
    for i in range(len(numbers)):
        if i >= 0 and i <= 10:
            if numbers[i] < 0:
                result.append(numbers[i])
    return result