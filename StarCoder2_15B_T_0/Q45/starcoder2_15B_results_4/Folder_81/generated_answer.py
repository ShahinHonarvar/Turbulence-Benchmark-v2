def palindromes_between_indices(string):
    letters = [c for c in string if c.isalpha()]
    palindromes = set()
    for i in range(len(letters) - 2):
        for j in range(i + 2, min(len(letters), i + 7)):
            palindrome = ''.join(letters[i:j])
            if palindrome.lower() == palindrome[::-1].lower():
                palindromes.add(palindrome)
    return palindromes