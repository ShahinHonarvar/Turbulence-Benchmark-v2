def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_lr_truncatable_prime(n):
        s = str(n)
        while len(s) > 1:
            if not is_prime(int(s[1:])) or not is_prime(int(s[:-1])):
                return False
            s = s[1:-1]
        return True
    x = numbers[97]
    result = [i for i in range(10, x + 1) if '0' not in str(i) and is_lr_truncatable_prime(i)]
    return sorted(result, reverse=True)