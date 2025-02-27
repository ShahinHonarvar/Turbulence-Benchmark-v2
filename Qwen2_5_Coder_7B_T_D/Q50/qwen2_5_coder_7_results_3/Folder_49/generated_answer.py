from collections import defaultdict

def if_contains_anagrams(lst):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    count = 0
    anagram_dict = defaultdict(list)
    for word in lst:
        if len(word) >= 3:
            anagram_dict[word.lower()].append(word)
    for key, value in anagram_dict.items():
        if len(value) > 1:
            count += len(value) * (len(value) - 1) // 2
    return count >= 59