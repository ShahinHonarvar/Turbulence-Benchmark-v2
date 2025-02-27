from itertools import permutations

def palindromes_between_indices(s):
    subset = s[2:5]
    unique_letters = set(subset.lower())
    palindromes = set()
    for length in range(3, len(unique_letters) + 1):
        for perm in permutations(unique_letters, length):
            palindrome = ''.join(perm)
            if palindrome.lower() == palindrome[::-1].lower():
                palindromes.add(palindrome.lower())
    return palindromes