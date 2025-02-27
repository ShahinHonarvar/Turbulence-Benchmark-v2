def find_second_largest_num(lst):
    if len(lst) < 10:
        return None
    top1 = top2 = float('-inf')
    for num in lst[:10]:
        if num > top1:
            top2 = top1
            top1 = num
        elif top2 < num < top1:
            top2 = num
    return top2 if top2 != float('-inf') else None