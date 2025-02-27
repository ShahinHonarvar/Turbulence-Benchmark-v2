def palindrome_of_length_n(s):
    set_palindromes = set()
    s = s.lower()
    for i in range(len(s) - 95):
        substring = s[i:i + 96]
        if substring.isalpha() and substring == substring[::-1]:
            set_palindromes.add(substring)
    return set_palindromes