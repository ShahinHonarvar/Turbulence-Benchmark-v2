from itertools import permutations

def palindromes_between_indices(s):
    substring = s[4:9]
    letters = ''.join(filter(str.isalpha, substring)).lower()
    palindromes = set()
    for i in range(5, len(letters) + 1):
        for perm in set(permutations(letters, i)):
            candidate_palindrome = ''.join(perm)
            if candidate_palindrome == candidate_palindrome[::-1]:
                palindromes.add(candidate_palindrome)
    return palindromes