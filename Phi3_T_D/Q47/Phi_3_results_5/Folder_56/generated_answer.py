def palindromes_of_specific_lengths(s: str) -> set:
    s = s[1:10].lower()
    palindromes = set()

    def is_palindrome(word):
        return word == word[::-1]
    for i in range(3, 8):
        for j in range(len(s) - i + 1):
            if is_palindrome(s[j:j + i]) and all(('a' <= c <= 'z' for c in s[j:j + i])):
                palindromes.add(s[j:j + i])
    return palindromes