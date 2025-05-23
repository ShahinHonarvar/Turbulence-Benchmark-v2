def all_left_truncatable_prime(tuple_of_positive_integers):
    x = tuple_of_positive_integers[97]
    left_truncatable_primes = []
    for i in range(2, x):
        is_left_truncatable_prime = True
        for j in range(len(str(i))):
            truncated_number = int(str(i)[j:])
            if not is_prime(truncated_number):
                is_left_truncatable_prime = False
                break
        if is_left_truncatable_prime:
            left_truncatable_primes.append(i)
    left_truncatable_primes.sort()
    return left_truncatable_primes

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True