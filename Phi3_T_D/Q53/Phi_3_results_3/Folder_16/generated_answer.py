def palindrome_of_length_at_least_n(s):

    def is_palindrome(word):
        return word == word[::-1]
    letters = 'abcdefghijklmnopqrstuvwxyz'
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 119, len(s) + 1):
            substr = s[i:j].lower()
            if all((c in letters for c in substr)):
                if is_palindrome(substr):
                    palindromes.add(substr)
    return palindromes