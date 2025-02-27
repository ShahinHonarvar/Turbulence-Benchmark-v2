from collections import defaultdict

def if_contains_anagrams(lst):
    anagrams = defaultdict(list)
    for word in lst:
        word = word.lower()
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word))
            anagrams[sorted_word].append(word)
    return any((len(v) >= 2 for v in anagrams.values())) and sum((len(v) * (len(v) - 1) // 2 for v in anagrams.values())) >= 10