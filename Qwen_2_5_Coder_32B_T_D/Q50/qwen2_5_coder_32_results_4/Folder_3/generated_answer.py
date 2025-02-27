from collections import defaultdict

def if_contains_anagrams(words):
    count = 0
    anagrams = defaultdict(list)
    for word in words:
        word_lower = word.lower()
        if len(word_lower) >= 3:
            anagrams[''.join(sorted(word_lower))].append(word_lower)
    for grouped_words in anagrams.values():
        count += len(grouped_words) * (len(grouped_words) - 1) // 2
        if count >= 30:
            return True
    return False