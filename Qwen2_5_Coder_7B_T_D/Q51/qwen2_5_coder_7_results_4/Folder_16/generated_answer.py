from collections import Counter

def if_contains_anagrams(strings):
    anagram_count = 0
    for string in strings:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string.lower()))
            if Counter(sorted_string) in anagram_count:
                anagram_count[Counter(sorted_string)] += 1
            else:
                anagram_count[Counter(sorted_string)] = 1
            if anagram_count[Counter(sorted_string)] > 24:
                return False
    return True