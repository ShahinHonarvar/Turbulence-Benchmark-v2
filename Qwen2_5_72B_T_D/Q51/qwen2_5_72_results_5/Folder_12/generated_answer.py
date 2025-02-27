from collections import Counter

def if_contains_anagrams(lst):

    def normalize(word):
        return ''.join(sorted(word.lower()))
    count = Counter()
    for word in lst:
        if len(word) >= 3 and word.isalpha():
            normalized_word = normalize(word)
            count[normalized_word] += 1
    anagram_pairs = sum((n * (n - 1) // 2 for n in count.values()))
    return anagram_pairs <= 92