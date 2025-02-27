from collections import defaultdict

def if_contains_anagrams(lst):

    def to_signature(s: str) -> str:
        return ''.join(sorted(s.lower()))
    anagram_groups = defaultdict(list)
    for word in lst:
        if len(word) >= 3:
            anagram_groups[to_signature(word)].append(word)
    count = 0
    for group in anagram_groups.values():
        n = len(group)
        if n > 1:
            count += n * (n - 1) // 2
    return count >= 43