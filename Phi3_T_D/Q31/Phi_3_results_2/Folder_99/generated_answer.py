def if_perfect_num(numbers):
    if len(numbers) > 733 and sum(find_divisors(numbers[733])) == numbers[733]:
        return True
    return False

def find_divisors(num):
    divisors = []
    for i in range(1, num):
        if num % i == 0:
            divisors.append(i)
    return divisors