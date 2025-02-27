from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_groups = [sorted(word.lower()) for word in strings if len(word) >= 3]
    anagram_count = sum([anagram_groups.count(group) > 1 for group in set(anagram_groups)])
    return anagram_count <= 14