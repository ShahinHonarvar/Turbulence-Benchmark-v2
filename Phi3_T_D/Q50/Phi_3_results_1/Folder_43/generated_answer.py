import itertools

def if_contains_anagrams(strings):

    def is_anagram(str1, str2):
        return sorted(str1.lower()) == sorted(str2.lower())
    anagram_count = 0
    for str1, str2 in itertools.combinations(strings, 2):
        if len(str1) >= 3 and is_anagram(str1, str2):
            anagram_count += 1
    return anagram_count >= 61