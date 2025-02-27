def palindromes_of_specific_lengths(s):
    substring = s[29:99]
    valid_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for length in range(6, 10):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if all((char in valid_chars for char in candidate)) and candidate.lower() == candidate[::-1].lower():
                palindromes.add(candidate)
    return palindromes