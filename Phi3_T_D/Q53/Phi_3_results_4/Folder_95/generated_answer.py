def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    length = 35
    while length <= len(s):
        for start in range(len(s) - length + 1):
            substring = s[start:start + length]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
        length += 1
    return palindromes