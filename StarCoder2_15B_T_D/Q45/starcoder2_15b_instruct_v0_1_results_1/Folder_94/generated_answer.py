def palindromes_between_indices(string):
    letters = sorted(set(string[3:5].lower()))
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 1, len(letters)):
            palindrome = letters[i] + letters[j] + letters[j] + letters[i]
            palindromes.add(palindrome)
    return palindromes