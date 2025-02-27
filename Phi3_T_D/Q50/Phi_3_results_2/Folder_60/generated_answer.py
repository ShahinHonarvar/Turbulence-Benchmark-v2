from collections import defaultdict

def if_contains_anagrams(lst):
    anagrams = defaultdict(list)
    for item in lst:
        key = ''.join(sorted(item.lower()))
        anagrams[key].append(item)
    pairs = [items for items in anagrams.values() if len(items) >= 2 and len(items[0]) >= 3]
    return len(pairs) >= 60