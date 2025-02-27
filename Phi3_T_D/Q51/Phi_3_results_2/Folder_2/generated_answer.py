from collections import defaultdict

def if_contains_anagrams(lst):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    max_allowed_pairs = 81
    grouped_anagrams = defaultdict(list)
    for word in lst:
        if len(word) < 3:
            continue
        key = ''.join(sorted(word.lower()))
        grouped_anagrams[key].append(word)
    anagram_count = 0
    for anagrams in grouped_anagrams.values():
        pairs = sum(range(len(anagrams)))
        anagram_count += pairs
        if anagram_count > max_allowed_pairs:
            return False
    return True