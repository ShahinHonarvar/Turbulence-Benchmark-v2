def find_primes_between_indices(nums):
    start_index = 57
    end_index = 64
    prime_nums = []
    for i, num in enumerate(nums):
        if i < start_index or i > end_index:
            continue
        if num > 1:
            for j in range(2, num):
                if num % j == 0:
                    break
            else:
                prime_nums.append(num)
    return sorted(prime_nums, reverse=True)