def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = numbers[55]
    truncatable_primes = []
    for num in range(10, x + 1):
        s = str(num)
        if '0' in s:
            continue
        trunc_prime = True
        for i in range(1, len(s) - 1):
            if not is_prime(int(s[i:])) or not is_prime(int(s[:-i])):
                trunc_prime = False
                break
        if trunc_prime and is_prime(int(s)) and is_prime(int(s[::-1])):
            truncatable_primes.append(num)
    return truncatable_primes