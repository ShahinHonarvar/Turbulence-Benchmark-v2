from itertools import permutations

def palindromes_between_indices(s):
    start, end = (3, 8)
    letters = s[start:end + 1].lower()
    palindromes = set()
    for length in range(6, len(letters) + 1, 2):
        for perm in permutations(letters, length):
            palindrome = ''.join(perm)
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes