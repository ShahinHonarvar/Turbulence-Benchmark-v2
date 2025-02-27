def is_prime(n):
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def all_left_right_truncatable_prime(input_tuple):
    x = input_tuple[0]
    result = []
    for num in range(10, x + 1):
        if is_prime(num):
            num_str = str(num)
            for i in range(1, len(num_str)):
                if not is_prime(int(num_str[i:])) or not is_prime(int(num_str[:len(num_str) - i])):
                    break
            else:
                result.append(num)
    result.sort(reverse=True)
    return result