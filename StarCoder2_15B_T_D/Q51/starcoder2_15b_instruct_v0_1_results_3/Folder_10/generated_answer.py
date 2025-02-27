import re

def if_contains_anagrams(strings):
    anagrams = {}
    for string in strings:
        string = re.sub('[^a-zA-Z]+', '', string).lower()
        if len(string) >= 3:
            anagram_key = ''.join(sorted(string))
            anagrams[anagram_key] = anagrams.get(anagram_key, 0) + 1
    return len(anagrams) <= 21