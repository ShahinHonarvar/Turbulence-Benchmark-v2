def all_left_right_truncatable_prime(nums):
    x = nums[57]
    truncatable_primes = []
    for i in range(2, x + 1):
        is_truncatable_prime = True
        for j in range(len(str(i)) - 1):
            left_truncation = int(str(i)[j:])
            right_truncation = int(str(i)[:len(str(i)) - j])
            if left_truncation % 2 == 0 or right_truncation % 2 == 0:
                is_truncatable_prime = False
                break
        if is_truncatable_prime:
            truncatable_primes.append(i)
    truncatable_primes.sort(reverse=True)
    return truncatable_primes