def all_left_right_truncatable_prime(x):
    if len(x) < 2:
        return []
    left_truncatable_prime = []
    right_truncatable_prime = []
    for i in range(len(x)):
        if i == 0:
            if x[i] in [2, 3, 5, 7]:
                left_truncatable_prime.append(x[i])
        elif x[i] in [1, 3, 7, 9] and x[i - 1] % 2 != 0 and (x[i - 1] % 3 != 0) and (x[i - 1] % 5 != 0) and (x[i - 1] % 7 != 0):
            left_truncatable_prime.append(x[i])
    for i in range(len(x) - 1, -1, -1):
        if i == len(x) - 1:
            if x[i] in [2, 3, 5, 7]:
                right_truncatable_prime.append(x[i])
        elif x[i] in [1, 3, 7, 9] and x[i + 1] % 2 != 0 and (x[i + 1] % 3 != 0) and (x[i + 1] % 5 != 0) and (x[i + 1] % 7 != 0):
            right_truncatable_prime.append(x[i])
    left_right_truncatable_prime = []
    for i in left_truncatable_prime:
        if i in right_truncatable_prime:
            left_right_truncatable_prime.append(i)
    left_right_truncatable_prime.sort(reverse=True)
    return left_right_truncatable_prime