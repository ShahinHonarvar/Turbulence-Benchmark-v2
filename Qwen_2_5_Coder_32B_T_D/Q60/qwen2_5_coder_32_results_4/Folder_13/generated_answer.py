def all_left_right_truncatable_prime(numbers):
    is_prime = lambda n: all((n % i for i in range(2, int(n ** 0.5) + 1))) if n > 1 else False
    x = numbers[784]
    result = []
    for num in range(10, x + 1):
        num_str = str(num)
        if '0' in num_str:
            continue
        valid = True
        for i in range(1, len(num_str) - 1):
            if not is_prime(int(num_str[i:-i])) or not is_prime(int(num_str[i:])):
                valid = False
                break
        if valid and is_prime(num):
            result.append(num)
    return result