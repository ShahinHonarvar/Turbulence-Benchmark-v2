from collections import defaultdict

def if_contains_anagrams(strings):

    def create_signature(s):
        return ''.join(sorted(s.lower()))
    counter = defaultdict(int)
    for string in strings:
        if len(string) >= 3:
            counter[create_signature(string)] += 1
    anagram_pairs = sum((count * (count - 1) // 2 for count in counter.values() if count > 1))
    return anagram_pairs >= 16