def is_perfect_num(num):
    return num == sum([i for i in range(1, num) if num % i == 0])

def if_perfect_num(num_list):
    try:
        return is_perfect_num(num_list[321])
    except IndexError:
        return False