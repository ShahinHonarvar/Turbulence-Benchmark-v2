def palindromes_between_indices(s):

    def is_palindrome(s):
        return s == s[::-1]
    s = s[3:9]
    english_letters = 'abcdefghijklmnopqrstuvwxyz'
    raw_letters = ''.join((c for c in s.lower() if c in english_letters))
    palindromes = set()
    for length in range(4, len(raw_letters) + 1):
        for start in range(len(raw_letters) - length + 1):
            candidate = raw_letters[start:start + length]
            if is_palindrome(candidate):
                palindromes.add(candidate)
    return palindromes