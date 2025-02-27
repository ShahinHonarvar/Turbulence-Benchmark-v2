from collections import defaultdict

def if_contains_anagrams(lst):
    anagrams = defaultdict(list)
    for word in lst:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            anagrams[sorted_word].append(word)
    count = 0
    for key, value in anagrams.items():
        if len(value) > 1:
            count += len(value) * (len(value) - 1) // 2
    return count <= 36