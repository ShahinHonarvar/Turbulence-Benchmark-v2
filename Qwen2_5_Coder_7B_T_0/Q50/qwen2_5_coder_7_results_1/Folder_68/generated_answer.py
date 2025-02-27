from collections import defaultdict

def if_contains_anagrams(lst):
    anagrams = defaultdict(list)
    for word in lst:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            anagrams[sorted_word].append(word)
    for group in anagrams.values():
        if len(group) >= 2:
            if len(group) * (len(group) - 1) // 2 >= 9:
                return True
    return False