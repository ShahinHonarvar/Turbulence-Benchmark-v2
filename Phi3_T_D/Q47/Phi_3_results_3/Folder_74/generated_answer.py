def palindromes_of_specific_lengths(s):

    def is_palindrome(subs):
        return subs.lower() == subs.lower()[::-1]
    palindromes = {subs for i in range(30, 85 - min(12, len(s) - 31) + 2) for j in range(i + 12, min(i + 21, len(s) - 30) + 1) if is_palindrome(s[i:j])}
    return {p for p in palindromes if p.isalpha()}