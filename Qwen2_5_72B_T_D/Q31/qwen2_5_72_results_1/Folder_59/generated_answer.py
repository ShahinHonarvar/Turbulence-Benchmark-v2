def if_perfect_num(nums):

    def is_perfect(n):
        sum = 1
        i = 2
        while i * i <= n:
            if n % i:
                i += 1
            else:
                sum += i
                if i * i != n:
                    sum += n // i
                i += 1
        return sum == n and n != 1
    return is_perfect(nums[2]) if len(nums) > 2 else False