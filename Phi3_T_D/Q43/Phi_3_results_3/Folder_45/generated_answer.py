def find_primes_between_indices(nums):
    start_index = 23
    end_index = 40
    primes = []
    for num in nums[start_index:end_index]:
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                primes.append(num)
    return sorted(primes)