def palindromes_between_indices(string):
    string = string.lower()
    letters = [ch for ch in string[1:6] if ch.isalpha()]
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i, len(letters)):
            palindrome = letters[i:j + 1]
            if len(palindrome) >= 4 and palindrome == palindrome[::-1]:
                palindromes.add(''.join(palindrome))
    return palindromes