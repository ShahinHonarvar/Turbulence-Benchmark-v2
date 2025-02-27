def palindromes_of_specific_lengths(s):

    def is_palindrome(t):
        return t == t[::-1]
    s = s[32:80]
    result = set()
    for i in range(len(s)):
        for j in range(i + 35, i + 42):
            if j <= len(s):
                candidate = s[i:j].lower()
                if candidate.isalpha() and is_palindrome(candidate):
                    result.add(candidate)
    return result