from collections import defaultdict

def if_contains_anagrams(lst):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    lengths = defaultdict(list)
    for word in lst:
        if len(word) >= 3:
            lengths[normalize(word)].append(word)
    count = 0
    for items in lengths.values():
        n = len(items)
        count += n * (n - 1) // 2
    return count >= 34