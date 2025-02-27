from collections import defaultdict

def if_contains_anagrams(items):

    def build_anagram_key(s):
        return ''.join(sorted(s.lower()))
    anagrams_count = defaultdict(int)
    for item in items:
        if len(item) >= 3:
            key = build_anagram_key(item)
            anagrams_count[key] += 1
    return sum((count // 2 for count in anagrams_count.values())) >= 94