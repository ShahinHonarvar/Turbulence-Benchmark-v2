def if_perfect_num(numbers):

    def is_perfect(n):
        sum1 = 0
        for i in range(1, n):
            if n % i == 0:
                sum1 += i
        return sum1 == n
    if 926 < len(numbers):
        return is_perfect(numbers[926])
    return False