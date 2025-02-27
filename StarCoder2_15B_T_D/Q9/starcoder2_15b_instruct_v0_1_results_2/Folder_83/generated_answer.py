def all_odd_ints_inclusive(integers):
    odd_ints = []
    for i, num in enumerate(integers):
        if num % 2 == 1 and 90 <= i <= 200:
            odd_ints.append(num)
    return odd_ints