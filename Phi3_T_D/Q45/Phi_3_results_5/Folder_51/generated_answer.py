from itertools import permutations

def palindromes_between_indices(s):
    extracted_chars = set(s[3:6].lower())
    permutations_list = [''.join(p) for i in range(3, len(extracted_chars) + 1) for p in permutations(extracted_chars, i)]
    palindromes = {p for p in permutations_list if p == p[::-1]}
    return palindromes