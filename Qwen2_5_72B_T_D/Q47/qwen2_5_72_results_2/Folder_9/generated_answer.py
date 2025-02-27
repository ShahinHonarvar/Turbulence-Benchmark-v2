def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    s = s[:301]
    result = set()
    for i in range(50, 61):
        for j in range(len(s) - i + 1):
            sub = s[j:j + i]
            if sub.isalpha() and is_palindrome(sub):
                result.add(sub)
    return result