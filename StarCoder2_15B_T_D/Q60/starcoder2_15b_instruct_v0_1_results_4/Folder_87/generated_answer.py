def all_left_right_truncatable_prime(tup):
    x = tup[39]
    left_truncatable_primes = [2, 3, 5, 7]
    for i in range(10, x + 1):
        is_left_truncatable = True
        for j in range(len(str(i)) - 1):
            truncated_num = int(str(i)[j + 1:])
            if not is_prime(truncated_num):
                is_left_truncatable = False
                break
        if is_left_truncatable:
            left_truncatable_primes.append(i)
    right_truncatable_primes = []
    for i in left_truncatable_primes:
        is_right_truncatable = True
        for j in range(len(str(i)) - 1):
            truncated_num = int(str(i)[:-j - 1])
            if not is_prime(truncated_num):
                is_right_truncatable = False
                break
        if is_right_truncatable:
            right_truncatable_primes.append(i)
    return sorted(right_truncatable_primes, reverse=True)

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True