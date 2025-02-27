def palindromes_of_specific_lengths(s):

    def is_palindrome(w):
        return w.lower() == w.lower()[::-1]
    result = set()
    if len(s) <= 74:
        s = s[10:75]
    else:
        s = s[10:74]
    for i in range(len(s)):
        for j in range(i + 6, min(len(s) + 1, i + 9)):
            substring = s[i:j]
            if substring.isalpha() and is_palindrome(substring):
                result.add(substring.lower())
    return result