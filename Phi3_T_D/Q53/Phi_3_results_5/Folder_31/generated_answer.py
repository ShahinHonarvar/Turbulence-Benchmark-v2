def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 33, len(s) + 1):
            if all((c.isalpha() for c in s[i:j])) and s[i:j] == s[i:j][::-1]:
                palindromes.add(s[i:j])
    return palindromes