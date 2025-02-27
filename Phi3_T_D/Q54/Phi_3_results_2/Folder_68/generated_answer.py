def all_right_truncatable_prime(numbers):
    max_value = numbers[1]
    highest_digits = (2, 3, 5, 7)

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable(n):
        while n > 0:
            if not is_prime(n):
                return False
            n //= 10
        return True

    def truncatable_primes(max_val, base=highest_digits):
        if max_val == 0:
            return [[]]
        if max_val < base[0]:
            return []
        sub_problems = truncatable_primes(max_val // 10)
        primes = []
        for primes_list in sub_problems:
            for digit in base:
                if digit < max_val + 1 and (not primes_list or primes_list[-1] < digit):
                    if is_right_truncatable(digit * 10 + primes_list[0]):
                        primes.append([digit] + primes_list[:])
        return primes
    return sorted(map(''.join, reversed(truncatable_primes(max_value, highest_digits))), reverse=True)