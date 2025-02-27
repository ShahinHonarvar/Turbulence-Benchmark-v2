def palindromes_between_indices(string):
    chars = [c for c in string if c.isalpha()]
    palindromes = set()
    for i in range(len(chars) - 3):
        for j in range(i + 3, len(chars) + 1):
            palindrome = ''.join(chars[i:j])
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome.lower())
    return palindromes