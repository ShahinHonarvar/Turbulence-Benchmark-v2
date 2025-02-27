def all_left_right_truncatable_prime(nums):
    x = nums[85]
    primes = [2, 3, 5, 7]
    for num in range(11, x + 1):
        if all((int(digit) != 0 for digit in str(num))):
            is_prime = True
            for i in range(len(str(num))):
                if int(str(num)[:len(str(num)) - i]) not in primes or int(str(num)[i:]) not in primes:
                    is_prime = False
                    break
            if is_prime:
                primes.append(num)
    return sorted(primes)