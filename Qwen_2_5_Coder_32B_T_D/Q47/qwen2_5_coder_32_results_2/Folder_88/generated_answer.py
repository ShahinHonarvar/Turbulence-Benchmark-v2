def palindromes_of_specific_lengths(s):
    s = s[11:88].lower()
    palindromes = set()
    for i in range(len(s) - 3):
        for l in range(4, 6):
            if i + l <= len(s):
                sub = s[i:i + l]
                if sub == sub[::-1] and sub.isalpha():
                    palindromes.add(sub)
    return palindromes