def palindromes_of_specific_lengths(s):

    def is_palindrome(t):
        return t == t[::-1]
    s = s[:6]
    result = set()
    for i in range(3, 6):
        for j in range(len(s) - i + 1):
            candidate = s[j:j + i].lower()
            if candidate.isalpha() and is_palindrome(candidate):
                result.add(candidate)
    return result