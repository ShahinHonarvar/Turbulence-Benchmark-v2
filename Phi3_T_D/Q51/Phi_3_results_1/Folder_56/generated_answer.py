from collections import Counter
        from itertools import combinations
    from itertools import combinations

def if_contains_anagrams(strings):

    def count_letters(s):
        return Counter((char.lower() for char in s if char.isalpha()))

    def are_anagram_pairs(l_n_c):
        anagrams = lambda s: any((count1 == count2 for count1, count2 in l_n_c))
        return sum((anagrams(pair[0]) and are_anagram_pairs(l_n_c + [count_letters(pair[1])]) for pair in combinations(strings, 2)))
    letter_counts = [count_letters(s) for s in strings if len(s) >= 3]
    return are_anagram_pairs(letter_counts) <= 11