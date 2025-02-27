from collections import defaultdict

def if_contains_anagrams(strings):

    def are_anagrams(s1, s2):
        return len(s1) >= 3 and len(s2) >= 3 and (sorted(s1.lower()) == sorted(s2.lower()))
    anagram_pairs = defaultdict(list)
    for string in strings:
        for key in anagram_pairs:
            if are_anagrams(string, key):
                anagram_pairs[key].append(string)
                break
        else:
            sorted_str = ''.join(sorted(string.lower()))
            anagram_pairs[sorted_str].append(string)
    return any((len(v) >= 2 for v in anagram_pairs.values()))