def if_perfect_num(num_list):

    def divisor_sum(num):
        return sum((d for d in range(1, num) if num % d == 0))
    return divisor_sum(num_list[410]) == num_list[410]