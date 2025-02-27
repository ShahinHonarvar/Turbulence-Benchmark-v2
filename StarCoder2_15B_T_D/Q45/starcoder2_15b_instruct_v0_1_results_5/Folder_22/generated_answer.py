def palindromes_between_indices(string):
    letters = [ch for ch in string[5:7].lower() if ch.isalpha()]
    palindromes = set()
    for i in range(len(letters) - 2):
        for j in range(i + 2, len(letters)):
            palindrome = letters[i] + letters[i + 1] + letters[j]
            palindromes.add(palindrome)
    return palindromes