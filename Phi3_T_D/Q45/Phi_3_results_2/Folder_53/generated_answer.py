from itertools import permutations
    from collections import Counter

def palindromes_between_indices(s):

    def is_palindrome(s):
        return s == s[::-1]
    sub_string = s[4:10]
    sub_string_count = Counter(sub_string.lower())
    possible_characters = ''.join([c for c, count in sub_string_count.items() if count >= 2])
    permutations_list = list()
    for length in range(6, len(possible_characters) + 1):
        for p in permutations(possible_characters, length):
            permutations_list.append(''.join(p))
    palindromes = set()
    for p in permutations_list:
        palindromes.add(p + p[::-1])
    return {p for p in palindromes if is_palindrome(p)}