def palindromes_between_indices(string):
    letters = [letter for letter in string if letter.isalpha()]
    letters_lower = [letter.lower() for letter in letters]
    palindromes = set()
    for i in range(3, 8):
        for j in range(i + 1, 8):
            for permutation in permutations(letters_lower[i:j]):
                palindrome = ''.join(permutation)
                if len(palindrome) >= 5 and palindrome == palindrome[::-1]:
                    palindromes.add(palindrome)
    return palindromes