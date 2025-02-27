def palindromes_of_specific_lengths(s):
    s = s[14:91].lower()
    palindromes = set()
    for i in range(len(s) - 54):
        for l in range(55, 72):
            if i + l > len(s):
                break
            sub = s[i:i + l]
            if sub.isalpha() and sub == sub[::-1]:
                palindromes.add(sub)
    return palindromes