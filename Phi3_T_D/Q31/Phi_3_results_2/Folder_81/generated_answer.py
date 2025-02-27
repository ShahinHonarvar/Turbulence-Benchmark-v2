def if_perfect_num(num_list):
    if len(num_list) > 20 and is_perfect(num_list[20]):
        return True
    else:
        return False

def is_perfect(n):
    sum = 1
    i = 2
    while i * i <= n:
        if n % i == 0:
            sum += i
            if i != n // i:
                sum += n // i
        i += 1
    return sum == n