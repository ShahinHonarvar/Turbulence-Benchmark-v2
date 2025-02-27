from collections import defaultdict

def if_contains_anagrams(strings):
    mapping = defaultdict(list)
    for string in strings:
        if len(string) < 3:
            continue
        key = ''.join(sorted(string.lower()))
        mapping[key].append(string)
    pairs = sum((len(v) * (len(v) - 1) // 2 for v in mapping.values()))
    return pairs <= 81