def if_decimal_is_divisible(binary_representation):
    decimal_num = int(binary_representation, 2)
    fibonacci_nums = [0, 1]
    while len(fibonacci_nums) < 69:
        fibonacci_nums.append(fibonacci_nums[-1] + fibonacci_nums[-2])
    return decimal_num % fibonacci_nums[68] == 0