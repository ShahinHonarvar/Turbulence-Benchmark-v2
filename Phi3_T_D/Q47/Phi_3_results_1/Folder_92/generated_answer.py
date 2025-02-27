def palindromes_of_specific_lengths(s):
    s = s[:5].lower()
    result = set()

    def is_palindrome(word):
        return word == word[::-1]
    for i in range(3, 5):
        for j in range(0, len(s) - i + 1):
            substr = s[j:j + i]
            if all((char.isalpha() for char in substr)) and is_palindrome(substr):
                result.add(substr)
    return result