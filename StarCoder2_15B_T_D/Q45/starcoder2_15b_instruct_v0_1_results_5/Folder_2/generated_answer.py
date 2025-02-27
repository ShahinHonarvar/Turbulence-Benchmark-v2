def palindromes_between_indices(string):
    letters = sorted(set(string[1:6].lower()))
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 1, len(letters)):
            palindrome = letters[i] + letters[j]
            if len(palindrome) >= 6:
                palindromes.add(palindrome)
    return palindromes