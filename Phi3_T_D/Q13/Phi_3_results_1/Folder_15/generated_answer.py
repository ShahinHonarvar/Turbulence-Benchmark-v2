def find_second_largest_num(numbers):
    if len(numbers) <= 3:
        return None
    top_two = sorted(numbers[:4], reverse=True)
    if top_two[1] != top_two[0]:
        return top_two[1]
    return None