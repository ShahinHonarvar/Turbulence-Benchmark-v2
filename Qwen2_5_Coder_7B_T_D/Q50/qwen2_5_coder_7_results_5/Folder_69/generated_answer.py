from collections import defaultdict

def if_contains_anagrams(lst):
    anagrams = defaultdict(list)
    for word in lst:
        sorted_word = ''.join(sorted(word.lower()))
        if len(word) >= 3:
            anagrams[sorted_word].append(word)
    count = 0
    for word_list in anagrams.values():
        if len(word_list) > 1:
            count += len(word_list) * (len(word_list) - 1) // 2
    return count >= 188