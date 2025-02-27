def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    max_num = numbers[11] if len(numbers) > 11 else None
    if max_num is None:
        raise ValueError('The tuple should contain at least 12 positive integers.')
    left_truncatable = set(['2', '3', '5', '7'])
    right_truncatable = {'2', '3', '5', '7'}

    def is_truncatable(num_str):
        for i in range(1, len(num_str)):
            if int(num_str[i:]) not in left_truncatable or int(num_str[:-i]) not in right_truncatable:
                return False
        return True
    return sorted([i for i in range(2, max_num + 1) if is_prime(i) and is_truncatable(str(i))])