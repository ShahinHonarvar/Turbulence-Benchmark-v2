def sum_ints_div_by_either_nums(ints_list: list) -> int:
    filtered_ints = filter(lambda i: i % 553 == 0 or i % 737 == 0, ints_list[543:585])
    return sum(filtered_ints) if filtered_ints else 0