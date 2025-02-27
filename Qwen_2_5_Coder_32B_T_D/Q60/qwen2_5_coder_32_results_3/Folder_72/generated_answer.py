def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = numbers[31]
    lr_truncatables = []
    for num in range(23, x + 1):
        snum = str(num)
        if '0' in snum:
            continue
        is_lr_truncatable = True
        for i in range(1, len(snum)):
            if not is_prime(int(snum[i:])) or not is_prime(int(snum[:-i])):
                is_lr_truncatable = False
                break
        if is_lr_truncatable and is_prime(num):
            lr_truncatables.append(num)
    return sorted(lr_truncatables, reverse=True)