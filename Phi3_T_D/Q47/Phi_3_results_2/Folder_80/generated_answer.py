def palindromes_of_specific_lengths(s):

    def is_palindrome(subs):
        return subs.lower() == subs[::-1].lower() and all((c.isalpha() for c in subs))
    pali_set = {s[i:j] for i in range(35, 89) for j in range(i + 23, i + 34 + 1) if is_palindrome(s[i:j])}
    return pali_set