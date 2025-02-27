from collections import defaultdict

def if_contains_anagrams(strings):

    def count_anagrams(s):
        key = ''.join(sorted(filter(str.isalpha, s.lower())))[::-1]
        return len(s) >= 3 and key
    anagram_counts = defaultdict(int)
    for s in strings:
        anagram_counts[count_anagrams(s)] += 1
    return sum((count * (count - 1) // 2 for count in anagram_counts.values())) <= 49