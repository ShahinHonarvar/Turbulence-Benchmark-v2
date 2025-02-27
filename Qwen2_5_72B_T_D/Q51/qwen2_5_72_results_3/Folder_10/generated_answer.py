from collections import Counter

def if_contains_anagrams(words):

    def canonical_form(word):
        return ''.join(sorted(word.lower()))
    count = Counter()
    for word in words:
        if len(word) >= 3 and word.isalpha():
            count[canonical_form(word)] += 1
    anagram_pairs = sum((k * (k - 1) // 2 for k in count.values()))
    return anagram_pairs <= 21