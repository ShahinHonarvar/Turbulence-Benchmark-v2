from collections import defaultdict

def if_contains_anagrams(words):
    anagrams = defaultdict(list)
    for word in words:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            anagrams[sorted_word].append(word)
    return any((len(v) >= 2 for v in anagrams.values())) and len([v for v in anagrams.values() if len(v) >= 2]) >= 3