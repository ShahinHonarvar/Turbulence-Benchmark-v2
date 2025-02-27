def palindromes_of_specific_lengths(s):
    s = s[11:94].lower()
    palindromes = set()
    for i in range(len(s) - 33):
        for j in range(33, 55):
            if i + j <= len(s):
                sub = s[i:i + j]
                if sub.isalpha() and sub == sub[::-1]:
                    palindromes.add(sub)
    return palindromes