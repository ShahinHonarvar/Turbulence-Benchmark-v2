def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 93):
        sub = s[i:i + 94]
        if sub.isalpha() and sub == sub[::-1]:
            palindromes.add(sub)
    return palindromes