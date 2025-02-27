from collections import Counter

def if_contains_anagrams(string_list):
    counter = Counter()
    for string in string_list:
        if len(string) >= 3:
            normalized = ''.join(sorted(string.lower()))
            counter[normalized] += 1
    return sum((v * (v - 1) // 2 for v in counter.values())) <= 91