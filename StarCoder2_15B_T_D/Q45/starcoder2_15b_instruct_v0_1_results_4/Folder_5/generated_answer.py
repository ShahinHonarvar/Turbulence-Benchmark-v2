def palindromes_between_indices(text):
    letters = [ch for ch in text if ch.isalpha()]
    palindromes = set()
    for i in range(4, len(letters) - 3):
        for j in range(i + 1, len(letters) + 1):
            palindrome = ''.join(letters[i:j])
            if len(palindrome) >= 4 and palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes