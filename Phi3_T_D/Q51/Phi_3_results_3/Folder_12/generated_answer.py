from collections import Counter

def if_contains_anagrams(strings):

    def count_three_or_more(s):
        return Counter(filter(lambda x: x.isalpha() and len(x) >= 3, s.lower()))
    anagram_counts = [count_three_or_more(s) for s in strings]
    pairs = 0
    for i, anagrams_i in enumerate(anagram_counts):
        for j in range(i + 1, len(anagrams_i)):
            if anagrams_i == anagram_counts[j]:
                pairs += 1
                if pairs > 92:
                    return False
    return True