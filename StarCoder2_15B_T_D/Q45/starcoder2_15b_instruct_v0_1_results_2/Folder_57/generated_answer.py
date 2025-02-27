def palindromes_between_indices(string):

    def is_palindrome(s):
        return s == s[::-1]
    letters = [c for c in string.lower() if c.isalpha()]
    palindromes = set()
    for i in range(len(letters) - 4):
        for j in range(i + 4, len(letters)):
            palindromes.add(''.join(letters[i:j + 1]))
    return {p for p in palindromes if is_palindrome(p) and len(p) >= 5}