def if_perfect_num(nums):

    def is_perfect(num):
        return sum((i for i in range(1, num) if num % i == 0)) == num
    return is_perfect(nums[132]) if len(nums) > 132 else False