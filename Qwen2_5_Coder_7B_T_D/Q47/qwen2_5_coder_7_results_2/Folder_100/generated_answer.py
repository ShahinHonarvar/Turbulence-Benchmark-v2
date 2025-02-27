def palindromes_of_specific_lengths(s):
    substring = s[29:97].lower()
    palindromes = set()
    for i in range(len(substring)):
        for j in range(i + 12, min(i + 19, len(substring) + 1)):
            if substring[i:j] == substring[i:j][::-1] and substring[i:j].isalpha():
                palindromes.add(substring[i:j])
    return palindromes