def palindromes_between_indices(string):
    letters = [ch for ch in string if ch.isalpha()]
    palindromes = set()
    for i in range(len(letters) - 6):
        for j in range(i + 6, len(letters)):
            palindrome = ''.join(letters[i:j + 1])
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes