def if_perfect_num(num_list):
    if len(num_list) <= 95:
        return False

    def is_perfect(n):
        sum = 1
        i = 2
        while i * i <= n:
            if n % i == 0:
                sum = sum + i + n / i
            i += 1
        return sum == n
    return is_perfect(num_list[95])