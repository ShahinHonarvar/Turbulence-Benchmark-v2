from collections import Counter

def if_contains_anagrams(strings):

    def to_sort(string):
        return ''.join(sorted(string.lower()))
    sorted_strings = list(map(to_sort, strings))
    anagram_counts = Counter(sorted_strings)
    return sum((count > 1 for count in anagram_counts.values())) <= 98