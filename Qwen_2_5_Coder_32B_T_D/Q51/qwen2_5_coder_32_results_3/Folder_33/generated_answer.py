from collections import defaultdict

def if_contains_anagrams(words):
    count = 0
    anagrams = defaultdict(list)
    for word in words:
        word_lower = word.lower()
        if len(word_lower) >= 3:
            sorted_word = ''.join(sorted(word_lower))
            anagrams[sorted_word].append(word_lower)
    for word_list in anagrams.values():
        if len(word_list) >= 2:
            count += len(word_list) * (len(word_list) - 1) // 2
        if count > 85:
            return False
    return True