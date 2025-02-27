def all_left_right_truncatable_prime(input_tuple):
    x = input_tuple[784]
    truncatable_primes = []
    for i in range(2, x + 1):
        is_truncatable = True
        for j in range(len(str(i)) - 1):
            left_truncation = int(str(i)[j + 1:])
            right_truncation = int(str(i)[:len(str(i)) - j - 1])
            if not (is_prime(left_truncation) and is_prime(right_truncation)):
                is_truncatable = False
                break
        if is_truncatable:
            truncatable_primes.append(i)
    truncatable_primes.sort()
    return truncatable_primes

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True