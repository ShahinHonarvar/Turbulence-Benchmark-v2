from collections import defaultdict

def if_contains_anagrams(words):
    count = 0
    anagrams = defaultdict(list)
    for word in words:
        word_lower = word.lower()
        if len(word_lower) >= 3:
            sorted_word = ''.join(sorted(word_lower))
            anagrams[sorted_word].append(word_lower)
    for groups in anagrams.values():
        if len(groups) > 1:
            count += len(groups) * (len(groups) - 1) // 2
    return count <= 147