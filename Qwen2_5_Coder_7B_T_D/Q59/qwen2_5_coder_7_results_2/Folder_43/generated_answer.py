def all_left_truncatable_prime(nums):
    x = nums[89]
    primes = [2, 3, 5, 7]
    left_truncatable_primes = []
    for num in range(11, x, 2):
        if '0' not in str(num):
            all_prime = True
            for i in range(len(str(num))):
                if int(str(num)[i:]) not in primes:
                    all_prime = False
                    break
            if all_prime:
                left_truncatable_primes.append(num)
                primes.append(num)
    left_truncatable_primes.sort(reverse=True)
    return left_truncatable_primes