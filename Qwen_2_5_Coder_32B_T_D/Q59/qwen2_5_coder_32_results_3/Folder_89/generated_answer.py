def all_left_truncatable_prime(numbers):
    x = numbers[97]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable(n):
        s = str(n)
        if '0' in s:
            return False
        for i in range(1, len(s)):
            if not is_prime(int(s[i:])):
                return False
        return True
    result = [i for i in range(2, x) if is_left_truncatable(i)]
    return sorted(result, reverse=True)