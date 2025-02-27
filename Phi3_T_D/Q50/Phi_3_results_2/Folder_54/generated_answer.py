from collections import defaultdict

def if_contains_anagrams(strings):
    anagrams_count = 0
    sorted_strings = {}
    for string in strings:
        if len(string) >= 3 and string.lower() not in sorted_strings:
            sorted_string = ''.join(sorted(string.lower()))
            anagrams = [s for s in strings if ''.join(sorted(s.lower())) == sorted_string and s.lower() != string.lower()]
            sorted_strings[string.lower()] = len(anagrams) + 1
            anagrams_count += len(anagrams)
    return anagrams_count >= 74