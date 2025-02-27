from collections import defaultdict

def if_contains_anagrams(strings):

    def is_anagram(str1, str2):
        return sorted(str1.lower()) == sorted(str2.lower())
    anagram_count = defaultdict(list)
    for string in strings:
        if len(string) >= 3:
            sorted_str = tuple(sorted(string.lower()))
            anagram_count[sorted_str].append(string)
    pairs_count = 0
    for anagrams in anagram_count.values():
        pairs_count += len(anagrams) * (len(anagrams) - 1) // 2
    return pairs_count >= 8 * 2