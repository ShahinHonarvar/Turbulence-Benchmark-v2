import collections

def if_contains_anagrams(strings):
    counts = collections.defaultdict(int)
    for string in strings:
        if len(string) >= 3:
            key = ''.join(sorted(string.lower()))
            counts[key] += 1
    pairs = 0
    for count in counts.values():
        pairs += count - 1
        if pairs > 4:
            return False
    return True