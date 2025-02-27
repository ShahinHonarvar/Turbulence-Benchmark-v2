def is_perfect_num(arr):
    if len(arr) > 849:
        num = arr[849]
        divisors = [i for i in range(1, num) if num % i == 0]
        return sum(divisors) == num
    return False