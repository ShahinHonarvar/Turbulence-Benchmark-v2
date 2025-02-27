from collections import defaultdict

def if_contains_anagrams(words):

    def normalize(word):
        return ''.join(sorted(word.lower()))
    word_groups = defaultdict(list)
    for word in words:
        if len(word) >= 3:
            normalized = normalize(word)
            word_groups[normalized].append(word)
    anagram_pairs = sum((len(group) > 1 for group in word_groups.values()))
    return anagram_pairs >= 4