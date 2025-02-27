from itertools import combinations

def if_contains_anagrams(lst):

    def count_chars(s):
        char_count = {}
        for char in s.lower():
            if char.isalpha() and len(char) >= 3:
                if char in char_count:
                    char_count[char] += 1
                else:
                    char_count[char] = 1
        return char_count
    anagram_count = 0
    for word1, word2 in combinations(lst, 2):
        if count_chars(word1) == count_chars(word2):
            anagram_count += 1
            if anagram_count > 131:
                return False
    return True