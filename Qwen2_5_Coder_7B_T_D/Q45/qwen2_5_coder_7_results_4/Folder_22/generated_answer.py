def palindromes_between_indices(s):
    letters = s[5:7]
    letters = letters.lower()
    letters = sorted(set(letters))
    if len(letters) < 3:
        return set()
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i, len(letters)):
            for k in range(j, len(letters)):
                palindrome = letters[i] + letters[j] + letters[k] + letters[j] + letters[i]
                palindromes.add(palindrome)
    return palindromes