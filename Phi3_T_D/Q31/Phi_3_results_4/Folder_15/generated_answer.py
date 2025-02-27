def is_perfect_num(num):
    if num < 2:
        return False
    divisors = [1]
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            divisors.append(i)
            if i != num // i:
                divisors.append(num // i)
    return sum(divisors) == num

def if_perfect_num(num_list):
    try:
        return is_perfect_num(num_list[10])
    except IndexError:
        return False