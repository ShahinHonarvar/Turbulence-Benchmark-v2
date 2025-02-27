def palindrome_of_length_at_least_n(s):
    ''.join((ch for ch in s if ch.isalpha())).lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 149, len(s)):
            substring = s[i:j + 1]
            if substring == substring[::-1]:
                palindromes.add(substring)
    palindromes