def all_left_truncatable_prime(nums):

    def is_truncatable_prime(num):
        num_str = str(num)
        return all((int(num_str[i:]) in primes for i in range(len(num_str))))
    primes = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43}
    x = nums[43]
    return sorted(filter(is_truncatable_prime, range(2, x)))