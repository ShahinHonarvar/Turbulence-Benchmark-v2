from collections import defaultdict

def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    count = 0
    anagram_dict = defaultdict(int)
    for string in strings:
        if len(string) >= 3:
            norm_string = normalize(string)
            count += anagram_dict[norm_string]
            anagram_dict[norm_string] += 1
    return count >= 86