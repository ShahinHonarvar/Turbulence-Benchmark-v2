def all_left_right_truncatable_prime(numbers):
    x = numbers[97]
    primes = set()

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    for num in range(2, x + 1):
        if '0' not in str(num) and is_prime(num):
            temp = num
            while temp > 9:
                temp //= 10
                if not is_prime(temp):
                    break
            else:
                temp = num
                while temp > 9:
                    temp %= 100
                    if not is_prime(temp):
                        break
                else:
                    primes.add(num)
    return sorted(primes, reverse=True)