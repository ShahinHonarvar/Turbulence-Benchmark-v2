from collections import Counter

def if_contains_anagrams(words):

    def normalize(word):
        return ''.join(sorted(word.lower()))
    anagrams = {}
    for word in words:
        if len(word) >= 3:
            normalized = normalize(word)
            if normalized in anagrams:
                anagrams[normalized].append(word)
            else:
                anagrams[normalized] = [word]
    pairs_count = 0
    for _, group in anagrams.items():
        if len(group) > 1:
            pairs_count += len(group) * (len(group) - 1) // 2
    return pairs_count <= 10