from collections import Counter

def if_contains_anagrams(strings):
    anagram_count = 0
    for string in strings:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string.lower()))
            if strings.count(sorted_string) > 1:
                anagram_count += 1
    return anagram_count >= 106