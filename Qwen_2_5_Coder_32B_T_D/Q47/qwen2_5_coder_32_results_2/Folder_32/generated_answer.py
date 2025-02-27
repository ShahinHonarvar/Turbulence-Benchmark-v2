def palindromes_of_specific_lengths(s):
    s = s[16:78].lower()
    palindromes = set()
    for i in range(len(s) - 42):
        for j in range(i + 42, min(i + 48, len(s))):
            if s[i:j + 1] == s[i:j + 1][::-1] and s[i:j + 1].isalpha():
                palindromes.add(s[i:j + 1])
    return palindromes