def palindromes_between_indices(string):
    valid_chars = [c for c in string.lower() if c.isalpha() and string.index(c) in range(2, 9)]
    palindromes = set()
    for i in range(len(valid_chars)):
        for j in range(i, len(valid_chars)):
            palindrome = valid_chars[i:j + 1]
            if len(palindrome) >= 6 and palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes