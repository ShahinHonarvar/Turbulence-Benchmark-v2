def palindromes_between_indices(string):
    letters = [letter for letter in string if letter.isalpha()]
    palindromes = set()
    for i in range(3, 7):
        for j in range(i + 1, 7):
            for permutation in itertools.permutations(letters, j - i + 1):
                palindrome = ''.join(permutation).lower()
                if palindrome == palindrome[::-1]:
                    palindromes.add(palindrome)
    return palindromes