from collections import defaultdict

def if_contains_anagrams(strings):

    def count_anagrams(s):
        return ''.join(sorted(s.lower()))
    string_to_anagrams = defaultdict(list)
    for string in strings:
        if len(string) >= 3:
            string_to_anagrams[count_anagrams(string)].append(string)
    anagram_pairs = sum([len(v) * (len(v) - 1) // 2 for v in string_to_anagrams.values()])
    return anagram_pairs >= 28