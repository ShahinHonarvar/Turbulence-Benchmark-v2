def if_perfect_num(num_list):

    def is_perfect(num):
        sum_of_divisors = sum((i for i in range(1, num) if num % i == 0))
        return sum_of_divisors == num
    if len(num_list) > 54:
        return is_perfect(num_list[54])
    else:
        return False