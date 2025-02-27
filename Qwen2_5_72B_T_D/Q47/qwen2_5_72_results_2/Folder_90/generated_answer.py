def palindromes_of_specific_lengths(s):

    def is_palindrome(s):
        return s == s[::-1]
    s = s[106:281]
    result = set()
    for i in range(len(s)):
        for j in range(i + 136, i + 152):
            if j <= len(s):
                candidate = s[i:j].lower()
                if candidate.isalpha() and is_palindrome(candidate):
                    result.add(candidate)
    return result