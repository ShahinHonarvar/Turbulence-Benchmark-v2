from collections import defaultdict

def if_contains_anagrams(words):
    anagram_count = defaultdict(int)
    for word in words:
        w = ''.join(sorted(word.lower()))
        if len(w) >= 3:
            anagram_count[w] += 1
    pairs = 0
    for count in anagram_count.values():
        pairs += count * (count - 1) // 2
        if pairs > 210:
            return False
    return True