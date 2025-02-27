def composite_nums_between_indices(integers):
    composites = set()
    for index in range(12, 93):
        number = integers[index]
        if number > 1:
            for i in range(2, int(number ** 0.5) + 1):
                if number % i == 0:
                    composites.add(number)
                    break
    return composites