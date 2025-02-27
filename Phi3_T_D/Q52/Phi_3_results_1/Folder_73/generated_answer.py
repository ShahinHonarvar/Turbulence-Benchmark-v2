def palindrome_of_length_n(s):
    length = len(s)
    s = s.lower()
    palindromes = set()
    for i in range(length - 40):
        sub = s[i:i + 41]
        if sub.isalpha() and sub == sub[::-1]:
            palindromes.add(sub)
    return palindromes