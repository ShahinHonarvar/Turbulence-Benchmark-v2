from collections import defaultdict

def if_contains_anagrams(lst):
    anagram_dict = defaultdict(list)
    for word in lst:
        word = word.lower()
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word))
            anagram_dict[sorted_word].append(word)
    for key, value in anagram_dict.items():
        if len(value) > 1:
            pairs = len(value) * (len(value) - 1) // 2
            if pairs >= 25:
                return True
    return False