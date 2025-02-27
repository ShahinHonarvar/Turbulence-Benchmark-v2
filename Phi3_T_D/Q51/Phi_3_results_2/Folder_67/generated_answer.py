from collections import defaultdict

def if_contains_anagrams(words):

    def normalize(word):
        word = word.lower()
        return ''.join(sorted(filter(str.isalpha, word)))
    anagram_groups = defaultdict(list)
    for word in words:
        if len(word) >= 3:
            normalized_word = normalize(word)
            anagram_groups[normalized_word].append(word)
    return sum((len(group) - 1 for group in anagram_groups.values() if len(group) > 1)) <= 10