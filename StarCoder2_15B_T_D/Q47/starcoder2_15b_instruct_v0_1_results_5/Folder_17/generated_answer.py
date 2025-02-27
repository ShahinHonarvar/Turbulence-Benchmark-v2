def palindromes_of_specific_lengths(s):
    palindromes = set()
    for i in range(22, 96):
        for j in range(i + 52, i + 56):
            if s[i:j] == s[i:j][::-1]:
                palindromes.add(s[i:j])
    return palindromes