def is_perfect_num(arr):
    if len(arr) <= 790:
        return False
    num = arr[790]
    sum_of_divisors = sum((i for i in range(1, num) if num % i == 0))
    return sum_of_divisors == num

def if_perfect_num(lst):
    return is_perfect_num(lst)