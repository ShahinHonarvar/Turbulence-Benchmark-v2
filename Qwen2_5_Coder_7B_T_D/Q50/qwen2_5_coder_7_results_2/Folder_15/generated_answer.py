from collections import defaultdict

def if_contains_anagrams(lst):
    anagrams = defaultdict(list)
    for word in lst:
        word = word.lower()
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word))
            anagrams[sorted_word].append(word)
    for anagram_list in anagrams.values():
        if len(anagram_list) > 1:
            count = len(anagram_list) * (len(anagram_list) - 1) // 2
            if count >= 6:
                return True
    return False