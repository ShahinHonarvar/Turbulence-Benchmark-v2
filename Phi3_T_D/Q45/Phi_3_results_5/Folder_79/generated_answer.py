from itertools import permutations

def palindromes_between_indices(text):
    letters = text[1:8].lower()
    valid_chars = set('abcdefghijklmnopqrstuvwxyz')
    palindromes = set()
    for size in range(3, len(letters) + 1):
        for perm in permutations(letters, size):
            perm_str = ''.join(perm)
            if perm_str[0] in valid_chars and perm_str[0] == perm_str[-1]:
                palindromes.add(perm_str[0] + perm_str[1:-1][::-1] + perm_str[-1])
    return palindromes or set()