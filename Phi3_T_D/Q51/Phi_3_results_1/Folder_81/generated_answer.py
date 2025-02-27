from collections import defaultdict

def if_contains_anagrams(string_list):

    def is_anagram(str1, str2):
        if len(str1) != len(str2):
            return False
        return sorted(str1.lower()) == sorted(str2.lower())

    def valid_anagram(s):
        return len(s) >= 3 and s.isalpha()
    anagrams_count = defaultdict(int)
    for s in string_list:
        if valid_anagram(s):
            key = ''.join(sorted(s.lower()))
            anagrams_count[key] += 1
    count = 0
    for key in anagrams_count:
        count += anagrams_count[key] * (anagrams_count[key] - 1) // 2
    return count <= 79