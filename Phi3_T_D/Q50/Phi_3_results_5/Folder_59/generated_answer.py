from collections import defaultdict
    from itertools import combinations

def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    anagram_counts = defaultdict(int)
    for string in strings:
        if len(string) >= 3:
            for anagram in anagram_counts:
                if is_anagram(string, anagram):
                    anagram_counts[anagram] += 1
                    break
            else:
                sorted_string = ''.join(sorted(string.lower()))
                anagram_counts[sorted_string] += 1
    return sum((1 for count in anagram_counts.values() if count * (count - 1) / 2 >= 10)) > 0