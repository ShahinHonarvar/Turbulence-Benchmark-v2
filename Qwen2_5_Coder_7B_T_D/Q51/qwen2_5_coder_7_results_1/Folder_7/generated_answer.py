from collections import defaultdict

def if_contains_anagrams(words):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    anagram_dict = defaultdict(list)
    for word in words:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            anagram_dict[sorted_word].append(word)
    anagram_pairs = 0
    for word_list in anagram_dict.values():
        n = len(word_list)
        if n > 1:
            anagram_pairs += n * (n - 1) // 2
    return anagram_pairs <= 445