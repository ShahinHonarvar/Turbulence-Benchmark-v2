def find_second_largest_num(numbers):
    if len(numbers) < 10:
        return None
    top_two = sorted(numbers[:10], reverse=True)[:2]
    if len(top_two) < 2:
        return None
    return top_two[1]