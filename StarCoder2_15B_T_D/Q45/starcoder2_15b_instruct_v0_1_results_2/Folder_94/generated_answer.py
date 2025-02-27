def palindromes_between_indices(string):
    letters = {letter for letter in string[3:5].lower() if letter.isalpha()}
    palindromes = set()
    for length in range(3, len(letters) + 1):
        for combination in itertools.permutations(letters, length):
            palindrome = ''.join(combination)
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes