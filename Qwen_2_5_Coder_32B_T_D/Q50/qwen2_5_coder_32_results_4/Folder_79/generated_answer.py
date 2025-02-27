from collections import defaultdict

def if_contains_anagrams(words):
    anagrams = defaultdict(list)
    for word in words:
        word_lower = word.lower()
        if len(word_lower) >= 3:
            sorted_word = ''.join(sorted(word_lower))
            anagrams[sorted_word].append(word_lower)
    count = 0
    for group in anagrams.values():
        count += len(group) * (len(group) - 1) // 2
        if count >= 40:
            return True
    return False