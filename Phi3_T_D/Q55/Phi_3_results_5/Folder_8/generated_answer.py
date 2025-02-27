def circular_binary_search(lst, target):
    left, right = (0, len(lst) - 1)
    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == target:
            return True
        elif lst[left] <= lst[mid]:
            if lst[left] <= target < lst[mid]:
                right = mid - 1
            else:
                left = mid + 1
        elif lst[mid] < target <= lst[right]:
            left = mid + 1
        else:
            right = mid - 1
    return False

def lists_with_product_equal_n(circular_list, target=-41):
    if len(circular_list) == 0:
        return []
    if circular_binary_search(circular_list, target):
        result = []
        for i in range(len(circular_list)):
            for j in range(i, len(circular_list)):
                temp = circular_list[i:j + 1] * circular_list[:j - i + 1]
                prod = prod(temp)
                if prod == target:
                    result.append(temp)
        return result
    return []

def prod(lst):
    result = 1
    for num in lst:
        result *= num
    return result