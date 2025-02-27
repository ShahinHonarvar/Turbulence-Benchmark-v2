def all_left_right_truncatable_prime(numbers):
    x = numbers[792]
    primes = [2, 3, 5, 7]
    truncatable_primes = []

    def is_prime(n):
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        str_n = str(n)
        return all((is_prime(int(str_n[i:])) and is_prime(int(str_n[:i + 1])) for i in range(len(str_n)))) and '0' not in str_n
    for num in range(2, x + 1):
        if is_prime(num) and is_truncatable(num):
            truncatable_primes.append(num)
    return truncatable_primes