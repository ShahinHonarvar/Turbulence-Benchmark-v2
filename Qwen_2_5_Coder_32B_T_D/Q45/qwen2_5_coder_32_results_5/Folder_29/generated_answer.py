from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join(sorted(filter(str.isalpha, s[2:10].lower())))
    palindromes = set()
    length = len(letters)
    for i in range(3, length // 2 + 1):
        for p in permutations(letters, i):
            p_str = ''.join(p)
            if p_str == p_str[::-1]:
                full_palindrome = p_str + p_str[-2::-1] if len(p_str) == i else p_str + p_str[::-1]
                palindromes.add(full_palindrome)
    return {p for p in palindromes if len(p) >= 6}