def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = numbers[23]
    result = []
    for num in range(11, x + 1):
        s = str(num)
        if '0' in s:
            continue
        left_right = True
        for i in range(1, len(s) - 1):
            if not (is_prime(int(s[i:])) and is_prime(int(s[:-i]))):
                left_right = False
                break
        if left_right and is_prime(int(s[1:])) and is_prime(int(s[:-1])):
            result.append(num)
    return sorted(result)