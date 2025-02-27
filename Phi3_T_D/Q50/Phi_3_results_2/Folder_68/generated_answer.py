from collections import defaultdict

def if_contains_anagrams(lst):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagrams = defaultdict(list)
    for word in lst:
        if len(word) >= 3:
            normalized = normalize(word)
            anagrams[normalized].append(word)
    pairs = 0
    for word_list in anagrams.values():
        pairs += sum(range(len(word_list)))
    return pairs >= 9