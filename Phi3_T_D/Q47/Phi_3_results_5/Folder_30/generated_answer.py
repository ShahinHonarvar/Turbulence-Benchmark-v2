def palindromes_of_specific_lengths(s):

    def is_palindrome(s):
        return s == s[::-1]

    def valid_palindrome(subs, l):
        if is_palindrome(subs.lower()) and subs.isalpha() and (55 <= len(subs) <= 71):
            return subs
        return None
    palindromes = set(filter(None, [valid_palindrome(s[i:j], j - i) for i in range(14, 91) for j in range(i + 55, i + 72)]))
    return palindromes