def all_right_truncatable_prime(x):
    result = []
    for i in range(len(str(x[42]))):
        num = int(str(x[42])[:-i])
        is_prime = True
        for j in range(2, int(num ** 0.5) + 1):
            if num % j == 0:
                is_prime = False
                break
        if is_prime:
            result.append(num)
    result.sort()
    return result