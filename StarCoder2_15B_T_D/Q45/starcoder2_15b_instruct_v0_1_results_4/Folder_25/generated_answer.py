def palindromes_between_indices(string):
    letters = [ch for ch in string if ch.isalpha()]
    palindromes = set()
    for i in range(1, len(letters) - 1):
        for j in range(i + 2, len(letters)):
            palindrome = letters[i:j + 1]
            if len(palindrome) >= 3 and palindrome == palindrome[::-1]:
                palindromes.add(''.join(palindrome))
    return palindromes