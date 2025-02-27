def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 98):
        if s[i] in 'abcdefghijklmnopqrstuvwxyz' and s[i + 98] in 'abcdefghijklmnopqrstuvwxyz' and (s[i:i + 99] == s[i:i + 99][::-1]):
            palindromes.add(s[i:i + 99])
    return palindromes