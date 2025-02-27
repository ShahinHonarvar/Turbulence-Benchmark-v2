def palindromes_of_specific_lengths(s):
    s = s[2:9].lower()
    palindromes = set()
    for i in range(len(s) - 2):
        for l in range(3, 5):
            if i + l <= len(s):
                sub = s[i:i + l]
                if sub == sub[::-1] and sub.isalpha():
                    palindromes.add(sub)
    return palindromes