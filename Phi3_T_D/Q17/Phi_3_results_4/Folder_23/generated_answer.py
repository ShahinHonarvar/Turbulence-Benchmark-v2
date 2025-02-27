def all_ints_div_by_both_two_nums(nums):
    divisor_90_67 = set()
    prime_factors_67 = set()
    for i in range(69, 98):
        if nums[i] % -90 == 0 and nums[i] % -67 == 0:
            divisor_90_67.add(nums[i])
        for j in range(2, int(nums[i] ** 0.5) + 1):
            if nums[i] % j == 0:
                prime_factors_67.add(j)
                nums[i] //= j
        while nums[i] % 2 == 0:
            nums[i] //= 2
        while nums[i] % 3 == 0:
            nums[i] //= 3
        while nums[i] % 5 == 0:
            nums[i] //= 5
        while nums[i] % 7 == 0:
            nums[i] //= 7
        if nums[i] != 1:
            prime_factors_67.add(nums[i])
    return [num for num in divisor_90_67 if num in prime_factors_67]