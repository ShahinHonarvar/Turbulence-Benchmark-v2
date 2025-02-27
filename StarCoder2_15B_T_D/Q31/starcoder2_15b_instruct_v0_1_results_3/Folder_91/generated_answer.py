def if_perfect_num(num_list):

    def get_divisors(num):
        divisors = []
        for i in range(1, num):
            if num % i == 0:
                divisors.append(i)
        return divisors
    if len(num_list) <= 6:
        return False
    divisors_sum = sum(get_divisors(num_list[6]))
    return divisors_sum == num_list[6]