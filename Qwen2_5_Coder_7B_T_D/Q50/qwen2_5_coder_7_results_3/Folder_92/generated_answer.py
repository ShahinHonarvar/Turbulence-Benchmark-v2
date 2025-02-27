from collections import defaultdict

def if_contains_anagrams(words):

    def sort_string(s):
        return ''.join(sorted(s.lower()))
    anagram_dict = defaultdict(list)
    for word in words:
        if len(word) >= 3:
            sorted_word = sort_string(word)
            anagram_dict[sorted_word].append(word)
    for anagrams in anagram_dict.values():
        if len(anagrams) >= 2:
            return True
    return False