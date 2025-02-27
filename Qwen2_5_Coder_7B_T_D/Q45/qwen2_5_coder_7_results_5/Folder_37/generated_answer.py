def palindromes_between_indices(s):
    letters = s[1:5].lower()
    letters = ''.join(sorted(letters))
    n = len(letters)
    palindromes = set()
    for i in range(n - 4, n):
        for j in range(n - 1, i - 1, -1):
            if letters[i:j + 1] == letters[i:j + 1][::-1]:
                palindromes.add(letters[i:j + 1])
    return palindromes