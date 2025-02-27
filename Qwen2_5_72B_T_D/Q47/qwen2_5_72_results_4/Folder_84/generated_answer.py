def palindromes_of_specific_lengths(s):

    def is_palindrome(s):
        return s == s[::-1]
    s = s[23:78]
    s = ''.join(filter(str.isalpha, s))
    palindromes = set()
    for start in range(len(s)):
        for end in range(start + 12, min(start + 41, len(s))):
            substring = s[start:end + 1]
            if is_palindrome(substring.lower()):
                palindromes.add(substring)
    return palindromes