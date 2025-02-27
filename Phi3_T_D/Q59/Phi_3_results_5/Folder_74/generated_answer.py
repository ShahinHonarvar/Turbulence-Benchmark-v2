def is_prime(n):
    if n <= 1:
        return False
    if n % 2 == 0 and n > 2:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[36]
    truncatables = []
    for num in range(2, x):
        if is_prime(num):
            num_str = str(num)
            truncatable = True
            for i in range(min(len(num_str), 9)):
                if not is_prime(int(num_str[i:])):
                    truncatable = False
                    break
            if truncatable:
                truncatables.append(num)
    return truncatables