def palindromes_between_indices(string):
    letters = [c for c in string if c.isalpha()]
    palindromes = set()
    for i in range(2, 5):
        for j in range(len(letters) - i + 1):
            palindrome = ''.join(letters[j:j + i]).lower()
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes