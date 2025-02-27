def palindromes_of_specific_lengths(s):
    palindromes = set()
    s = s[11:94].lower()
    for i in range(len(s) - 1):
        for j in range(i + 33, min(i + 55, len(s)) + 1):
            if s[i:j] == s[i:j][::-1] and s[i:j].isalpha():
                palindromes.add(s[i:j])
    return palindromes