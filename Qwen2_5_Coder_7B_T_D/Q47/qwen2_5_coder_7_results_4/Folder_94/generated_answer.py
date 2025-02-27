def palindromes_of_specific_lengths(s):
    s = s[40:95].lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 45, min(i + 52, len(s) + 1)):
            if s[i:j] == s[i:j][::-1] and s[i:j].isalpha():
                palindromes.add(s[i:j])
    return palindromes