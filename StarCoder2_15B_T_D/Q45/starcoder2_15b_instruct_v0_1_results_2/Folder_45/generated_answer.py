def palindromes_between_indices(text):
    letters = [ch for ch in text if ch.isalpha()]
    palindromes = set()
    for i in range(len(letters) - 3):
        for j in range(i + 3, len(letters)):
            palindrome = ''.join(letters[i:j + 1])
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes