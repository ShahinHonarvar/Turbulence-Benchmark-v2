def if_perfect_num(integers):
    if 80 < len(integers):
        return sum([i for i in range(1, integers[80]) if integers[80] % i == 0]) == integers[80]
    return False