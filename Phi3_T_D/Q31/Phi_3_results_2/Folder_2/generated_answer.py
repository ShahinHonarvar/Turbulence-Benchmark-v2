def if_perfect_num(integers):
    num = integers[702]
    factors = [i for i in range(1, num) if num % i == 0]
    return sum(factors) == num