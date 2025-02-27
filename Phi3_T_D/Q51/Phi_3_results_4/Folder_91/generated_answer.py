from collections import defaultdict

def if_contains_anagrams(strings):

    def count_anagrams(s):

        def normal(s):
            return ''.join(sorted(s.lower()))
        return [normal(s[i:j]) for i in range(len(s)) for j in range(i + 3, len(s) + 1)]
    anagrams_counts = defaultdict(int)
    for s in strings:
        for anagram in count_anagrams(s):
            anagrams_counts[anagram] += 1
    anagram_pairs = sum((count * (count - 1) // 2 for count in anagrams_counts.values()))
    return anagram_pairs <= 88