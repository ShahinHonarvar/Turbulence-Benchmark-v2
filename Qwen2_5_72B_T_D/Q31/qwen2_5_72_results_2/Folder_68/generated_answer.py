def if_perfect_num(numbers):

    def is_perfect(n):
        sum = 1
        i = 2
        while i * i <= n:
            if n % i:
                i += 1
            else:
                sum += i
                if i * i != n:
                    sum += n // i
                i += 1
        return sum == n and n != 1
    return is_perfect(numbers[3]) if len(numbers) > 3 else False