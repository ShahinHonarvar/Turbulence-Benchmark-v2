def if_perfect_num(num_list):
    if len(num_list) > 60 and is_perfect_number(num_list[60]):
        return True
    return False

def is_perfect_number(n):
    sum = 1
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            sum += i
            if i != n // i:
                sum += n // i
    return sum == n and n != 1