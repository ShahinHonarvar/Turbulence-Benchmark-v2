def palindromes_of_specific_lengths(s):

    def is_valid_palindrome(sub_s):
        sub_s = sub_s.lower()
        return sub_s == sub_s[::-1] and all(('a' <= c <= 'z' for c in sub_s))
    return {s[i:j + 1] for i in range(21) for j in range(i + 4, 21) if is_valid_palindrome(s[i:j + 1])}