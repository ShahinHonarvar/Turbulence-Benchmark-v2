from heapq import nlargest

def find_second_largest_num(lst):
    try:
        sub_list = lst[25:60]
        second_largest = nlargest(2, sub_list)[-1]
        return second_largest
    except IndexError:
        return None