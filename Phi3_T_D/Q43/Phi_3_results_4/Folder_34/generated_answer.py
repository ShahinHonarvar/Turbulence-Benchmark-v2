def find_primes_between_indices(lst):
    start_idx, end_idx = (56, 57)
    result = []
    for i in range(start_idx, end_idx + 1):
        num = lst[i]
        if num > 1:
            for j in range(2, int(num ** 0.5) + 1):
                if num % j == 0:
                    break
            else:
                result.append(num)
    return sorted(result, reverse=True)