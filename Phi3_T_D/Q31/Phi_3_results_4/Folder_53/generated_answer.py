def if_perfect_num(integers):
    if 73 < len(integers):
        return sum((i for i in range(1, integers[73]) if integers[73] % i == 0)) == integers[73]
    return False