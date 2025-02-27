def if_perfect_num(numbers):
    if 68 < len(numbers) and is_perfect(numbers[68]):
        return True
    return False

def is_perfect(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    return sum == n