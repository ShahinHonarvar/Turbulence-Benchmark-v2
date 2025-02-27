def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    string_length = len(s)
    for i in range(string_length):
        for j in range(i + 74, string_length + 1):
            substring = s[i:j]
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes