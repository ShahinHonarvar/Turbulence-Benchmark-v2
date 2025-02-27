from itertools import permutations

def palindromes_between_indices(s):
    s_slice = s[3:9]
    unique_letters = set(s_slice.lower())
    palindromes = set()
    for length in range(7, len(unique_letters) + 1):
        for perm in permutations(unique_letters, length):
            palindrome = ''.join(perm) + ''.join(perm[::-1])
            palindromes.add(palindrome.upper())
    return palindromes