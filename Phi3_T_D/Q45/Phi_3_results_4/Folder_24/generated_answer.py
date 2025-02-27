from itertools import permutations
    from itertools import product

def palindromes_between_indices(s):
    substring = s[2:10]
    char_count = {}
    for char in substring:
        if char.isalpha():
            char = char.lower()
            char_count[char] = char_count.get(char, 0) + 1
    palindromes = set()
    for permutation in product(char_count.keys(), repeat=4):
        for _ in range(4):
            palindromes.add(''.join(permutation))
    return palindromes