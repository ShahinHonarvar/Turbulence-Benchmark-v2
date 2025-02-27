from collections import defaultdict

def if_contains_anagrams(words):
    anagrams = defaultdict(list)
    for word in words:
        normalized = ''.join(sorted(word.lower()))
        if len(normalized) >= 3:
            anagrams[normalized].append(word)
    count = sum((len(v) * (len(v) - 1) // 2 for v in anagrams.values()))
    return count >= 144