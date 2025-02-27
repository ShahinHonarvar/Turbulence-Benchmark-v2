def palindromes_between_indices(string):
    allowed_chars = {c.lower() for c in string if c.isalpha() and 2 <= string.index(c) <= 9}
    palindromes = set()
    for length in range(7, len(allowed_chars) + 1):
        for combination in combinations(allowed_chars, length):
            palindrome = ''.join(combination)
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes