def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def is_truncatable_prime(n):
        s = str(n)
        return all((is_prime(int(s[i:])) and is_prime(int(s[:len(s) - i])) for i in range(len(s))))
    x = numbers[20]
    return sorted([i for i in range(2, x + 1) if is_truncatable_prime(i)], reverse=True)