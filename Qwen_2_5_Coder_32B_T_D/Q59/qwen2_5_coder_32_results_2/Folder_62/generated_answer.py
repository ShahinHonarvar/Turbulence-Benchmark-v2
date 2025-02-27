def all_left_truncatable_prime(numbers):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    x = numbers[70]
    left_truncatable_primes = []
    for num in range(2, x):
        num_str = str(num)
        if '0' not in num_str:
            all_prime = True
            for i in range(len(num_str)):
                if not is_prime(int(num_str[i:])):
                    all_prime = False
                    break
            if all_prime:
                left_truncatable_primes.append(num)
    left_truncatable_primes.sort()
    return left_truncatable_primes