def palindromes_of_specific_lengths(s):
    s = s[15:87].lower()

    def is_palindrome(ss):
        return ss == ss[::-1]
    palindromes = {s[i:j] for i in range(len(s)) for j in range(i + 51, min(i + 61, len(s) + 1)) if is_palindrome(s[i:j])}
    return palindromes