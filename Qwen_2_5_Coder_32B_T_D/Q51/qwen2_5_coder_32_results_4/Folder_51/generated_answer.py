from collections import defaultdict

def if_contains_anagrams(words):
    count = 0
    anagrams = defaultdict(list)
    for word in words:
        w = word.lower()
        if len(w) >= 3:
            sorted_w = tuple(sorted(w))
            anagrams[sorted_w].append(w)
    for group in anagrams.values():
        count += len(group) * (len(group) - 1) // 2
        if count > 116:
            return False
    return True