from itertools import combinations

def if_contains_anagrams(lst):

    def normalize(s):
        return ''.join(sorted(s.lower()))

    def get_anagrams(words):
        anagrams = {}
        for word in words:
            nw = normalize(word)
            if nw in anagrams:
                anagrams[nw].add(word)
            else:
                anagrams[nw] = {word}
        return anagrams
    anagram_pairs = 0
    anagram_dict = get_anagrams(lst)
    for keys in anagram_dict.keys():
        words = list(anagram_dict[keys])
        for pair in combinations(words, 2):
            if len(set(pair)) == 2:
                anagram_pairs += 1
    return anagram_pairs <= 423