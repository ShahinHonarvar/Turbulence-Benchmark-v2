def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    result = set()
    if len(s) > 299:
        s = s[1:300]
    for i in range(len(s)):
        for j in range(i + 3, min(i + 11, len(s) + 1)):
            sub = s[i:j]
            if sub.isalpha() and is_palindrome(sub):
                result.add(sub.lower())
    return result