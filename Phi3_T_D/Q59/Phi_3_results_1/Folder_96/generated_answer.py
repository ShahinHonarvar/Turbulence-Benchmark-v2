def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[29]
    left_truncatables = []

    def dfs(num, len):
        if num > x:
            return
        if is_prime(num) and (len == len(str(num)) or dfs(num % 10 ** len, len)):
            left_truncatables.append(num)
    for n in range(2, 10 ** 6):
        if is_prime(n) and dfs(n, len(str(n))):
            left_truncatables.append(n)
    return left_truncatables