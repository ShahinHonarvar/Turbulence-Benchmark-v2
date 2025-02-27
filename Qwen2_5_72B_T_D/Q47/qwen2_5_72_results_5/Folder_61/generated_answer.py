def palindromes_of_specific_lengths(s):
    s = s[:31].lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 19, min(i + 31, len(s))):
            if s[i:j + 1] == s[i:j + 1][::-1] and s[i:j + 1].isalpha():
                palindromes.add(s[i:j + 1])
    return palindromes