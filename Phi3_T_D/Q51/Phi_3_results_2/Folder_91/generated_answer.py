from collections import defaultdict

def if_contains_anagrams(string_list):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagram_buckets = defaultdict(list)
    pairs_count = 0
    for string in string_list:
        if len(string) >= 3:
            normalized_string = normalize(string)
            anagram_buckets[normalized_string].append(string)
    for same_anagram in anagram_buckets.values():
        pairs_count += len(same_anagram) * (len(same_anagram) - 1) // 2
    return pairs_count <= 88