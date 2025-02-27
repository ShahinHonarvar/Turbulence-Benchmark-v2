from collections import Counter

def if_contains_anagrams(lst):
    lst = [word.lower() for word in lst if len(word) >= 3]
    counter = Counter([''.join(sorted(word)) for word in lst])
    pairs = sum((count * (count - 1) // 2 for count in counter.values()))
    return pairs >= 85