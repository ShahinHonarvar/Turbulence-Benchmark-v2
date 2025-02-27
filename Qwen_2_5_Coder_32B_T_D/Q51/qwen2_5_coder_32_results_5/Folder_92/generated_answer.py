from collections import defaultdict

def if_contains_anagrams(lst):

    def sorted_word(word):
        return ''.join(sorted(word.lower()))
    anagram_counts = defaultdict(int)
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            w1, w2 = (lst[i], lst[j])
            if len(w1) >= 3 and len(w2) >= 3 and (sorted_word(w1) == sorted_word(w2)):
                anagram_counts[sorted_word(w1), sorted_word(w2)] += 1
    return sum(anagram_counts.values()) <= 34