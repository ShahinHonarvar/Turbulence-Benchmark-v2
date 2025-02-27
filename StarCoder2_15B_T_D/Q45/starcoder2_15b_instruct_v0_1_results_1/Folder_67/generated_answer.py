from itertools import permutations

def palindromes_between_indices(text):
    text = list(text)
    permutation_list = [''.join(p) for p in permutations(text[2:7])]
    palindrome_list = [p for p in permutation_list if p == p[::-1] and len(p) >= 5]
    return set(palindrome_list)