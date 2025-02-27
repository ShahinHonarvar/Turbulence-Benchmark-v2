def if_perfect_num(integers):
    return sum([i for i in range(1, integers[68]) if integers[68] % i == 0]) == integers[68]