from collections import defaultdict

def if_contains_anagrams(words):
    d = defaultdict(int)
    for word in words:
        word = word.lower()
        if len(word) >= 3:
            d[tuple(sorted(word))] += 1
    pairs = 0
    for count in d.values():
        if count > 1:
            pairs += count * (count - 1) // 2
            if pairs > 289:
                return False
    return True