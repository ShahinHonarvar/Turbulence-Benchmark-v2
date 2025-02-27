def palindromes_of_specific_lengths(s):

    def is_palindrome(t):
        return t == t[::-1]
    s = s[:31]
    s = ''.join(filter(str.isalpha, s))
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 20, min(len(s), i + 31)):
            candidate = s[i:j + 1].lower()
            if is_palindrome(candidate):
                palindromes.add(candidate)
    return palindromes