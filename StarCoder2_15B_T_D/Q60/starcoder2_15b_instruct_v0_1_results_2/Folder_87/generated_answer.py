def all_left_right_truncatable_prime(numbers):
    result = []
    x = numbers[39]

    def truncate(num):
        return int(str(num)[1:])

    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    for i in range(10, x + 1):
        num = i
        while num >= 10:
            if not is_prime(num):
                break
            num = truncate(num)
        else:
            if is_prime(num):
                result.append(i)
    result.sort(reverse=True)
    return result