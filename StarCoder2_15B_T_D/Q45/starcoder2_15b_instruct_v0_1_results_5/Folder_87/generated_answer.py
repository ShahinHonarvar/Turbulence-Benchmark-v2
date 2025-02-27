def palindromes_between_indices(string):
    letters = [ch for ch in string[3:10].lower() if ch.isalpha()]
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 2, len(letters)):
            palindrome = letters[i] + letters[j]
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes