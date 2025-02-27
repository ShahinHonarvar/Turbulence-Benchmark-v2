from collections import Counter

def if_contains_anagrams(strings):

    def count_anagrams(string):
        return Counter(sorted(string.lower()))
    anagram_dict = {}
    for string in strings:
        if len(string) >= 3:
            anagram_key = count_anagrams(string)
            if anagram_key in anagram_dict:
                anagram_dict[anagram_key].append(string)
            else:
                anagram_dict[anagram_key] = [string]
    anagram_pairs = sum((len(v) * (len(v) - 1) // 2 for v in anagram_dict.values() if len(v) > 1))
    return anagram_pairs >= 52