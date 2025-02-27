def palindromes_of_specific_lengths(s):
    s = s[16:78].lower()
    palindromes = set()
    for i in range(len(s) - 42):
        for length in range(43, 48):
            if s[i:i + length] == s[i:i + length][::-1]:
                palindromes.add(s[i:i + length])
    return palindromes