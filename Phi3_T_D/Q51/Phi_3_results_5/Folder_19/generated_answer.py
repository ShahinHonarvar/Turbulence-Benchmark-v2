from collections import defaultdict

def if_contains_anagrams(strings):

    def anagram_key(s):
        return ''.join(sorted((c.lower() for c in s if c.isalpha()))).ljust(69, ' ')
    anagram_groups = defaultdict(list)
    for string in strings:
        if len(string) >= 3:
            anagram_groups[anagram_key(string)].append(string)
    return sum((len(group) * (len(group) - 1) // 2 for group in anagram_groups.values())) <= 69