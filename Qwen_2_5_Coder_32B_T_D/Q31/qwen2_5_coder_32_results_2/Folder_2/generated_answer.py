def if_perfect_num(numbers):

    def is_perfect(n):
        if n < 2:
            return False
        sum = 1
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                sum += i
                if i != n // i:
                    sum += n // i
        return sum == n
    if len(numbers) < 703:
        return False
    return is_perfect(numbers[702])