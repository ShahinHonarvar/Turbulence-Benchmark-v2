from collections import defaultdict
    from itertools import permutations

def if_contains_anagrams(string_list):
    anagram_dict = defaultdict(list)
    for word in string_list:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            anagram_dict[sorted_word].append(word)

    def generate_permutations(lst):
        return [''.join(p) for p in permutations(lst) if p[0] == lst[0]]
    anagram_pairs = 0
    for sorted_word, words in anagram_dict.items():
        if len(words) > 1:
            for perm in generate_permutations(sorted_word):
                for w in words:
                    if perm in w.lower():
                        anagram_pairs += 1
                        break
    return anagram_pairs >= 136