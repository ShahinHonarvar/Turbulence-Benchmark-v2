def palindromes_of_specific_lengths(s):
    s = s[15:96]
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 20, min(i + 67, len(s) + 1)):
            sub = s[i:j]
            if sub.lower() == sub[::-1].lower() and sub.isalpha():
                palindromes.add(sub)
    return palindromes