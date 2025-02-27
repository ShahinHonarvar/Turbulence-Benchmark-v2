def palindrome_of_length_n(s):

    def is_alpha(char):
        return 'a' <= char <= 'z' or 'A' <= char <= 'Z'
    n = 49
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - n + 1):
        substr = s[i:i + n]
        if substr.isalpha() and substr == substr[::-1]:
            palindromes.add(substr)
    return palindromes