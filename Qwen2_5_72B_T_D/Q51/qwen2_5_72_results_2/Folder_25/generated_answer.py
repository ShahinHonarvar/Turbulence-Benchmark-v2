from collections import defaultdict

def if_contains_anagrams(words):

    def normalize(word):
        return ''.join(sorted(word.lower()))
    anagrams = defaultdict(int)
    for word in words:
        if len(word) >= 3:
            normalized = normalize(word)
            anagrams[normalized] += 1
    pairs = 0
    for count in anagrams.values():
        pairs += count * (count - 1) // 2
    return pairs <= 67