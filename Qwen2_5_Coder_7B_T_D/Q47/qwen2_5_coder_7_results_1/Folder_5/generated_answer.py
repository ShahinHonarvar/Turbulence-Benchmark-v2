def palindromes_of_specific_lengths(s):
    palindromes = set()
    substring = s[63:71].lower()
    for i in range(len(substring)):
        for j in range(i + 4, min(len(substring), i + 6)):
            sub = substring[i:j]
            if sub == sub[::-1]:
                palindromes.add(sub)
    return palindromes