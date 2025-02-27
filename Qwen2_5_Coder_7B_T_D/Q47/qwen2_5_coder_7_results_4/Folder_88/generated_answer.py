def palindromes_of_specific_lengths(s):
    s = s[11:88].lower()
    palindromes = set()
    for i in range(len(s) - 3):
        for j in range(i + 4, i + 6):
            if s[i:j] == s[i:j][::-1]:
                palindromes.add(s[i:j])
    return palindromes