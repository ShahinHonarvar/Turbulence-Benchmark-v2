def all_even_ints_exclusive(nums):

    def is_even(num):
        return num % 2 == 0

    def is_in_range(num):
        return 29 <= num < 53
    return [num for num in nums if is_even(num) and is_in_range(num)]