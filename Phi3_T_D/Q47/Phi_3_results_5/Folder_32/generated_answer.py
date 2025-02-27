def palindromes_of_specific_lengths(s):
    s = s[16:78].lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 43, min(i + 48, len(s) + 1)):
            if s[i:j] == s[i:j][::-1]:
                palindromes.add(s[i:j].upper())
    return palindromes