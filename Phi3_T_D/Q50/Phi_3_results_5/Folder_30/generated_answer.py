from collections import defaultdict

def if_contains_anagrams(strings):

    def is_anagram(str1, str2):
        return sorted(str1.lower()) == sorted(str2.lower())
    anagram_count = 0
    anagrams = defaultdict(list)
    for string in strings:
        key = ''.join(sorted(string.lower()))
        anagrams[key].append(string)
    for groups in anagrams.values():
        if len(groups) >= 2:
            anagram_count += len(groups) * (len(groups) - 1) // 2
    return anagram_count >= 78