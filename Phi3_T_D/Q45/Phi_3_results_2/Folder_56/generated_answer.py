from itertools import permutations

def palindromes_between_indices(s):
    s = s[5:10].lower()
    unique_chars = ''.join(set(s))
    palindromes = set()
    for length in range(5, 10):
        for perm in set(permutations(unique_chars, length)):
            palindrome = ''.join(perm)
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes