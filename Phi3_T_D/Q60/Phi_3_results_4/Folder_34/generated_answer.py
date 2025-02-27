def all_left_right_truncatable_prime(numbers_tuple):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def all_digit_truncatable(num):
        if num < 10 and is_prime(num):
            return num
        temp = str(num)
        for i in range(len(temp)):
            if num < 10 or not is_prime(int(temp[i:])) or (not is_prime(int(temp[:i + 1]))):
                return False
        return True
    x = numbers_tuple[18]
    left_right_truncatable_primes = []
    for num in range(2, x + 1):
        if all_digit_truncatable(num):
            left_right_truncatable_primes.append(num)
    return sorted(left_right_truncatable_primes, reverse=True)