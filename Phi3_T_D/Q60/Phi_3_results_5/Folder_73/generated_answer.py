def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_primes(numbers):
    x = numbers[97]
    primes = [i for i in range(2, x + 1) if is_prime(i)]
    truncatables = []
    for prime in primes:
        str_prime = str(prime)
        length = len(str_prime)
        left = right = prime
        for _ in range(length):
            if not is_prime(left):
                left = 0
                if right == prime:
                    break
                right //= 10
            if right == 0:
                break
            if not is_prime(right):
                left = 0
                if right == prime:
                    break
                right //= 10
        if left != 0 and right != 0:
            truncatables.append(prime)
    return sorted(truncatables)