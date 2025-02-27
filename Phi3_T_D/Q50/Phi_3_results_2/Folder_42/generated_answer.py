from collections import defaultdict

def if_contains_anagrams(strings):

    def is_anagram(str1, str2):
        return sorted(str1.lower()) == sorted(str2.lower())
    anagrams = defaultdict(list)
    for string in strings:
        if len(string) >= 3:
            key = ''.join(sorted(string.lower()))
            anagrams[key].append(string)
    count = 0
    for key, value in anagrams.items():
        if len(value) > 1:
            count += len(value) * (len(value) - 1) // 2
    return count >= 233