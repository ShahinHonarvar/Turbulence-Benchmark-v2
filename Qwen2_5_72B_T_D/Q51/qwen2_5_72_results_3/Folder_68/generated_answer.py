from collections import Counter

def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    count = Counter()
    for string in strings:
        if len(string) >= 3 and string.isalpha():
            count[normalize(string)] += 1
    anagram_pairs = sum((k * (k - 1) // 2 for k in count.values()))
    return anagram_pairs <= 94