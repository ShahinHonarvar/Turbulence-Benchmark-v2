def palindromes_between_indices(s):
    letters = s[5:7]
    letters = letters.lower()
    unique_letters = set(letters)
    palindromes = set()
    for i in range(1, len(letters)):
        for perm in permutations(unique_letters, i):
            palindrome = ''.join(perm) + ''.join(perm[::-1])
            if len(palindrome) >= 3:
                palindromes.add(palindrome)
    return palindromes