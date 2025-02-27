def all_left_right_truncatable_prime(tuple_of_positive_integers):
    x = tuple_of_positive_integers[97]
    truncatable_primes = []
    for i in range(2, x + 1):
        is_truncatable = True
        for j in range(len(str(i)) - 1):
            truncated_number = int(str(i)[j + 1:])
            if not is_prime(truncated_number):
                is_truncatable = False
                break
            truncated_number = int(str(i)[:-j - 1])
            if not is_prime(truncated_number):
                is_truncatable = False
                break
        if is_truncatable:
            truncatable_primes.append(i)
    return sorted(truncatable_primes)

def is_prime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True