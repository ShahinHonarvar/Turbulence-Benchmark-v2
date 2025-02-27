from collections import defaultdict

def if_contains_anagrams(lst):

    def simplify_word(word):
        return ''.join(sorted(word.lower()))
    anagram_map = defaultdict(int)
    count = 0
    for word in lst:
        if len(word) >= 3:
            simplified = simplify_word(word)
            count += anagram_map[simplified]
            anagram_map[simplified] += 1
    return count >= 39