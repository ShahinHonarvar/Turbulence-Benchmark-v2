def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 32):
        sub = s[i:i + 33]
        if sub == sub[::-1] and sub.isalpha():
            palindromes.add(sub)
    return palindromes