from collections import defaultdict

def if_contains_anagrams(lst):
    anagrams = defaultdict(list)
    for word in lst:
        if len(word) < 3:
            continue
        word = word.lower()
        sorted_word = ''.join(sorted(word))
        anagrams[sorted_word].append(word)
    pairs = 0
    for word_list in anagrams.values():
        if len(word_list) > 1:
            pairs += len(word_list) - 1
    return pairs >= 7