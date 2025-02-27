from collections import defaultdict

def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s).lower())
    anagrams_count = defaultdict(int)
    for string in strings:
        if len(string) >= 3:
            normalized = normalize(string)
            anagrams_count[normalized] += 1
    anagrams_pairs = sum((count * (count - 1) // 2 for count in anagrams_count.values()))
    return anagrams_pairs >= 46