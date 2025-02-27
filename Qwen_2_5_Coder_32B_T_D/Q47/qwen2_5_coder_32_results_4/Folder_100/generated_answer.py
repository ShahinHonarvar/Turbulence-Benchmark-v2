def palindromes_of_specific_lengths(s):
    s = s[29:97].lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(12, 19):
            if i + j <= len(s):
                sub = s[i:i + j]
                if sub.isalpha() and sub == sub[::-1]:
                    palindromes.add(sub)
    return palindromes