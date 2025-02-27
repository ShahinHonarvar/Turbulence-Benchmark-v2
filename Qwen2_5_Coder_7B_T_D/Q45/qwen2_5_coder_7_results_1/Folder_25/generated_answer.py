def palindromes_between_indices(s):
    letters = s[1:5]
    letters = letters.lower()
    letters_set = set(letters)
    palindromes = set()
    for i in range(3, len(letters_set) + 1):
        for combination in combinations(letters_set, i):
            for permutation in permutations(combination):
                palindrome = ''.join(permutation)
                if palindrome == palindrome[::-1]:
                    palindromes.add(palindrome)
    return palindromes