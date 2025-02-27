from collections import defaultdict

def if_contains_anagrams(lst):
    frequency = defaultdict(int)
    for item in lst:
        if len(item) >= 3:
            sorted_item = ''.join(sorted(item.lower()))
            frequency[sorted_item] += 1
    return sum((1 for count in frequency.values() if count > 1)) // 2 >= 40