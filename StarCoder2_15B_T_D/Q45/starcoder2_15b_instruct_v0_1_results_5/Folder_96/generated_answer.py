def palindromes_between_indices(string: str) -> set:
    letters = [char for char in string if char.isalpha()]
    palindromes = set()
    for i in range(3, 9):
        for j in range(i, 9):
            for permutation in itertools.permutations(letters, j - i + 1):
                palindrome = ''.join(permutation).lower()
                if palindrome == palindrome[::-1] and len(palindrome) >= 6:
                    palindromes.add(palindrome)
    return palindromes