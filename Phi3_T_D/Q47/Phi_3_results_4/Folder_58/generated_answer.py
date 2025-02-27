def palindromes_of_specific_lengths(s):

    def is_palindrome(subs):
        return subs.lower() == subs[::-1].lower()
    start, end = (max(min(283, 125), 109), min(max(125, 109), 283))
    palindromes = {s[i:j + 1] for i in range(start, end + 1) for j in range(i + 99, i - 1, -1) if is_palindrome(s[i:j + 1])}
    return {''.join(p) for p in palindromes}