def palindromes_between_indices(string):
    letters = [letter for letter in string if letter.isalpha()]
    palindromes = set()
    for i in range(3, 7):
        for j in range(i + 1, 7):
            for combination in combinations(letters, j - i + 1):
                palindrome = ''.join(combination).lower()
                if palindrome == palindrome[::-1] and len(palindrome) >= 4:
                    palindromes.add(palindrome)
    return palindromes