from collections import defaultdict

def if_contains_anagrams(strings):
    count = 0
    min_length = 3
    anagrams = defaultdict(list)
    for word in strings:
        if len(word) >= min_length:
            sorted_word = ''.join(sorted(word.lower()))
            anagrams[sorted_word].append(word)
    for a in anagrams.values():
        if len(a) > 1:
            count += len(a) // 2
    return count >= 144