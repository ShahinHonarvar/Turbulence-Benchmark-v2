def palindrome_of_length_at_least_n(s):
    set_palindromes = set()
    s = s.lower()
    for i in range(len(s)):
        for j in range(i + 31, len(s) + 1):
            substring = s[i:j]
            if substring.isalpha() and substring == substring[::-1]:
                set_palindromes.add(substring)
    return set_palindromes