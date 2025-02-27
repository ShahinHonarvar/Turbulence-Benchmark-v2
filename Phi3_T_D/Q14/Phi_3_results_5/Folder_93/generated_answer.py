def find_second_smallest_num(lst):
    start, end = (75, 88)
    return find_kth_smallest(lst, start, end, 2) if len(lst[start:end + 1]) >= 2 else None

def find_kth_smallest(lst, start, end, k):

    def partition(base_idx, end_idx):
        pivot = lst[end_idx]
        i = base_idx - 1
        for j in range(base_idx, end_idx):
            if lst[j] <= pivot:
                i += 1
                lst[i], lst[j] = (lst[j], lst[i])
        lst[i + 1], lst[end_idx] = (lst[end_idx], lst[i + 1])
        return i + 1

    def quickselect(base_idx, end_idx, position):
        if base_idx < end_idx:
            pivot_index = partition(base_idx, end_idx)
            if pivot_index == position:
                return lst[pivot_index]
            elif pivot_index < position:
                return quickselect(pivot_index + 1, end_idx, position)
            else:
                return quickselect(base_idx, pivot_index - 1, position)
        return lst[pivot_index]
    if start < end:
        return quickselect(start, end, k - 1)