from collections import defaultdict

def if_contains_anagrams(words):
    anagrams = defaultdict(list)
    for word in words:
        cleaned_word = ''.join(filter(str.isalpha, word.lower()))
        if len(cleaned_word) >= 3:
            sorted_word = tuple(sorted(cleaned_word))
            anagrams[sorted_word].append(cleaned_word)
    pair_count = sum((len(v) * (len(v) - 1) // 2 for v in anagrams.values() if len(v) > 1))
    return pair_count <= 24