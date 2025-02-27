def palindromes_of_specific_lengths(s):
    s = s[:8].lower()
    palindromes = set()
    for i in range(len(s) - 3):
        for length in range(4, 6):
            if s[i:i + length] == s[i:i + length][::-1]:
                palindromes.add(s[i:i + length])
    return palindromes