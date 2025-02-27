def all_left_right_truncatable_prime(numbers):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    x = numbers[370]
    truncatable_primes = []
    for num in range(1, x + 1):
        if is_prime(num):
            is_truncatable = True
            temp = num
            while temp >= 10:
                temp //= 10
                if not is_prime(temp):
                    is_truncatable = False
                    break
            temp = num
            while temp >= 10:
                temp %= 10 ** (len(str(temp)) - 1)
                if not is_prime(temp):
                    is_truncatable = False
                    break
            if is_truncatable:
                truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)