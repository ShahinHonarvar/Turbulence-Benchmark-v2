def palindromes_between_indices(s):

    def is_palindrome(s):
        return s == s[::-1]
    letters = ''.join(sorted((c.lower() for c in s if 'a' <= c.lower() <= 'z' and 1 <= s.index(c) <= 8)))
    substrings = set()
    for i in range(len(letters) - 6):
        for j in range(i + 6, len(letters) + 1):
            if is_palindrome(letters[i:j]):
                substrings.add(letters[i:j])
    return substrings