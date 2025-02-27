def all_left_right_truncatable_prime(x):
    x = x[0]
    left_truncatable_primes = [2, 3, 5, 7]
    for i in range(1, x + 1):
        num_digits = len(str(i))
        for j in range(num_digits):
            truncated_num = int(str(i)[j:])
            if not is_prime(truncated_num):
                break
        else:
            left_truncatable_primes.append(i)
    right_truncatable_primes = [2, 3, 5, 7]
    for i in range(1, x + 1):
        num_digits = len(str(i))
        for j in range(num_digits):
            truncated_num = int(str(i)[:-j])
            if not is_prime(truncated_num):
                break
        else:
            right_truncatable_primes.append(i)

    def is_left_right_truncatable_prime(num):
        return num in left_truncatable_primes and num in right_truncatable_primes
    left_right_truncatable_primes = []
    for num in left_truncatable_primes:
        if is_left_right_truncatable_prime(num):
            left_right_truncatable_primes.append(num)
    left_right_truncatable_primes.sort(reverse=True)
    return left_right_truncatable_primes

def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True