def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 415):
        if s[i:i + 416] == s[i:i + 416][::-1]:
            palindromes.add(s[i:i + 416])
    return palindromes