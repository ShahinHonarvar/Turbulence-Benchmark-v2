def all_left_right_truncatable_prime(numbers):

    def is_truncatable_prime(num):
        if num < 10:
            return False
        if num in [2, 3, 5, 7]:
            return True
        return all((is_prime(int(str(num)[i:])) for i in range(len(str(num)))))
    x = numbers[78]
    truncatable_primes = [p for p in range(2, x + 1) if is_truncatable_prime(p)]
    truncatable_primes.sort(reverse=True)
    return truncatable_primes