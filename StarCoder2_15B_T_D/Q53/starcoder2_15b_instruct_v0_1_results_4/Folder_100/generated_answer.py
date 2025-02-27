def palindrome_of_length_at_least_n(s):
    palindromes = set()
    for i in range(len(s) - 48):
        for j in range(i + 48, len(s)):
            if s[i:j].lower() == s[i:j][::-1].lower():
                palindromes.add(s[i:j])
    return palindromes