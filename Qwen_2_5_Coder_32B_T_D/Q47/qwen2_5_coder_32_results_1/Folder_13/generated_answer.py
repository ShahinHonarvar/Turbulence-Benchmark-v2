def palindromes_of_specific_lengths(s):
    s = s[13:96].lower()
    palindromes = set()
    for i in range(len(s) - 56):
        for length in range(57, 61):
            if i + length <= len(s):
                sub = s[i:i + length]
                if sub.isalpha() and sub == sub[::-1]:
                    palindromes.add(sub)
    return palindromes