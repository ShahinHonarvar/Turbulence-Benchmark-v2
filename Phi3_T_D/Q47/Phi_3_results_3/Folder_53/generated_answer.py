def palindromes_of_specific_lengths(s):

    def expand_around_center(s, l, r):
        while l >= 0 and r < len(s) and is_english_letter(s[l]) and is_english_letter(s[r]):
            if s[l:r + 1].lower() == s[l:r + 1][::-1].lower():
                if 3 <= len(s[l:r + 1]) <= 10:
                    yield s[l:r + 1]
                l -= 1
                r += 1
            else:
                break

    def is_english_letter(c):
        return 'a' <= c.lower() <= 'z'

    def is_valid_palindrome(palindrome):
        length = len(palindrome)
        return 3 <= length <= 10
    palindromes_set = set()
    for i in range(1, 300):
        palindromes_set.update(expand_around_center(s, i, i))
        palindromes_set.update(expand_around_center(s, i, i + 1))
    return {p for p in palindromes_set if is_valid_palindrome(p)}