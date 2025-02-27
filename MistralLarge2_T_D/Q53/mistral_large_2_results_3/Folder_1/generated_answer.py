def palindrome_of_length_at_least_n(s):
    n = 29
    palindromes = set()
    s = ''.join((char for char in s if char.isalpha())).lower()
    for i in range(len(s)):
        for j in range(i + n, len(s) + 1):
            substring = s[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes