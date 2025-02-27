from collections import defaultdict

def if_contains_anagrams(strings_list):

    def normalize_string(s):
        return ''.join(sorted(s.lower().replace(' ', '')))
    anagram_dict = defaultdict(int)
    for s in strings_list:
        if len(s) >= 3:
            normalized_string = normalize_string(s)
            anagram_dict[normalized_string] += 1
    return sum((1 for count in anagram_dict.values() if count >= 2 and len(strings_list) * (len(strings_list) - 1) / 2 * count ** 2 >= 177))