def all_left_right_truncatable_prime(numbers):
    x = numbers[77]

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    truncatable_primes = []
    for i in range(1, x + 1):
        if is_prime(i):
            digits = [int(d) for d in str(i)]
            is_truncatable = True
            for j in range(len(digits) - 1):
                if not is_prime(int(''.join(map(str, digits[j:])))) or not is_prime(int(''.join(map(str, digits[:len(digits) - j])))):
                    is_truncatable = False
                    break
            if is_truncatable:
                truncatable_primes.append(i)
    truncatable_primes.sort(reverse=True)
    return truncatable_primes