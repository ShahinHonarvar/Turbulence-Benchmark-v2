def all_left_truncatable_prime(numbers):
    x = numbers[97]
    left_truncatable_prime = []
    for i in range(2, x):
        is_left_truncatable = True
        for j in range(len(str(i)) - 1):
            if int(str(i)[j + 1:]) % i != 0:
                is_left_truncatable = False
                break
        if is_left_truncatable:
            left_truncatable_prime.append(i)
    return sorted(left_truncatable_prime, reverse=True)