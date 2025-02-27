def palindromes_of_specific_lengths(s):

    def is_palindrome(s):
        return s == s[::-1]
    s = s[44:100]
    result = set()
    for i in range(13, 43):
        for j in range(len(s) - i + 1):
            candidate = s[j:j + i]
            if is_palindrome(candidate) and candidate.isalpha():
                result.add(candidate.lower())
    return result