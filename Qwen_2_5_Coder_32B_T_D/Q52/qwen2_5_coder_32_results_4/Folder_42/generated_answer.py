def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 278):
        sub = s[i:i + 279]
        if sub.isalpha() and sub == sub[::-1]:
            palindromes.add(sub)
    return palindromes