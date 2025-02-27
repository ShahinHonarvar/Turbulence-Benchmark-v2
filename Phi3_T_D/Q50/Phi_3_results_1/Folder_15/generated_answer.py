from collections import defaultdict

def if_contains_anagrams(lst):

    def count_chars(s):
        s = s.lower()
        count = defaultdict(int)
        for char in s:
            count[char] += 1
        return count

    def is_anagram(s1, s2):
        return count_chars(s1) == count_chars(s2)
    anagram_sets = defaultdict(list)
    for s in lst:
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s.lower()))
            anagram_sets[sorted_s].append(s)
    anagram_pairs = 0
    for anagram_list in anagram_sets.values():
        if len(anagram_list) > 1:
            pairs = sum(range(len(anagram_list)))
            anagram_pairs += pairs
    return anagram_pairs >= 4 * 2