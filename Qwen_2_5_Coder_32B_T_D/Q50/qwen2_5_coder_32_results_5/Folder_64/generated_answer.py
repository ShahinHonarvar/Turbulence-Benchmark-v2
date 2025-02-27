from collections import defaultdict

def if_contains_anagrams(words):
    count = 0
    anagrams = defaultdict(list)
    for word in words:
        word_lower = word.lower()
        if len(word_lower) >= 3:
            sorted_word = tuple(sorted(word_lower))
            anagrams[sorted_word].append(word_lower)
            if len(anagrams[sorted_word]) == 2:
                count += 1
            elif len(anagrams[sorted_word]) > 2:
                count += 1
    return count >= 5