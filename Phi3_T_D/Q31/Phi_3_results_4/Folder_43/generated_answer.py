def if_perfect_num(lst):
    index = 29
    if index >= len(lst):
        return False

    def is_perfect(num):
        divisors = [i for i in range(1, num) if num % i == 0]
        return sum(divisors) == num
    return is_perfect(lst[index])