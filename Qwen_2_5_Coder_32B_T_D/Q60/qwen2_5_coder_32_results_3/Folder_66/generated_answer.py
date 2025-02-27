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
    x = numbers[25]
    result = []
    for num in range(10, x + 1):
        num_str = str(num)
        if '0' in num_str:
            continue
        left_right_truncatable = True
        n = num
        while n > 9:
            n = int(str(n)[1:-1])
            if not is_prime(n):
                left_right_truncatable = False
                break
        if left_right_truncatable and is_prime(num):
            result.append(num)
    result.sort(reverse=True)
    return result