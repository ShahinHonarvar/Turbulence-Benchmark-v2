def is_perfect(num):
    if num < 2:
        return False
    divisors = [1]
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            divisors.append(i)
            if i != num // i:
                divisors.append(num // i)
    return sum(divisors) == num

def if_perfect_num(nums_list):
    if len(nums_list) > 49:
        return is_perfect(nums_list[49])
    else:
        return False