def all_left_right_truncatable_prime(nums):
    x = nums[97]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    lr_trunc_primes = []
    for num in range(11, x + 1):
        str_num = str(num)
        if '0' in str_num:
            continue
        is_lr_trunc_prime = True
        temp_num = num
        while len(str(temp_num)) > 1:
            temp_num //= 10
            if not is_prime(temp_num):
                is_lr_trunc_prime = False
                break
        temp_num = num
        while len(str(temp_num)) > 1:
            temp_num = int(str(temp_num)[:-1])
            if not is_prime(temp_num):
                is_lr_trunc_prime = False
                break
        if is_lr_trunc_prime and is_prime(num):
            lr_trunc_primes.append(num)
    return sorted(lr_trunc_primes, reverse=True)