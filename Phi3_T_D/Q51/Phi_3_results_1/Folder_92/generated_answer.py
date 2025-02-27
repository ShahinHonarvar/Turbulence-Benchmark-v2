from collections import Counter

def if_contains_anagrams(strings):

    def string_key(s):
        return ''.join(sorted(s.lower()))
    grouped_strings = {}
    for string in strings:
        if len(string) >= 3:
            key = string_key(string)
            if key in grouped_strings:
                grouped_strings[key].append(string)
            else:
                grouped_strings[key] = [string]
    anagram_pairs = 0
    for group in grouped_strings.values():
        if len(group) > 1:
            anagram_pairs += len(group) * (len(group) - 1) // 2
            if anagram_pairs > 34:
                return False
    return True