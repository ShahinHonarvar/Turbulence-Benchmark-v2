from collections import Counter

def if_contains_anagrams(strings):
    anagram_count = 0
    for string in strings:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string.lower()))
            if anagram_count > 84:
                return False
            anagram_count += 1
    return True