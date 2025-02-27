def all_right_truncatable_prime(input):
    numbers = input[0]
    x = numbers[65]

    def is_right_truncatable_prime(num):
        if num < 10 and is_prime(num):
            return True
        elif num < 10:
            return False
        else:
            return is_prime(num) and is_right_truncatable_prime(int(str(num)[:-1]))

    def is_prime(num):
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    result = []
    for num in range(x):
        if is_right_truncatable_prime(num):
            result.append(num)
    return sorted(result, reverse=True)