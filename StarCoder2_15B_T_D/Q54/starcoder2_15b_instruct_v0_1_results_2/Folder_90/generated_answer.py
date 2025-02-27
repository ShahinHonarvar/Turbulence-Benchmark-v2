def all_right_truncatable_prime(input_tuple):
    x = input_tuple[466]
    truncatable_primes = []
    for i in range(2, x):
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            for k in range(1, len(str(i))):
                if int(str(i)[:-k]) == 0:
                    break
                if not is_truncatable_prime(int(str(i)[:-k])):
                    is_prime = False
                    break
        if is_prime:
            truncatable_primes.append(i)
    return sorted(truncatable_primes, reverse=True)

def is_truncatable_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True