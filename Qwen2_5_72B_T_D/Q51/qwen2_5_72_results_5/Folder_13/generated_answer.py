from collections import Counter

def if_contains_anagrams(lst):

    def to_sorted_str(s):
        return ''.join(sorted(s.lower()))
    anagram_pairs = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3 and (to_sorted_str(lst[i]) == to_sorted_str(lst[j])):
                anagram_pairs.append((lst[i], lst[j]))
    return len(anagram_pairs) <= 54