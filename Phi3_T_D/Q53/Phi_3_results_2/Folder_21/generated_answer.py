def palindrome_of_length_at_least_n(s):

    def is_palindrome(word):
        return word == word[::-1]
    s_lower = s.lower()
    palindromes = set()
    length = 112
    while length <= len(s_lower):
        for i in range(len(s_lower) - length + 1):
            candidate = s_lower[i:i + length]
            if all((c.isalpha() for c in candidate)) and is_palindrome(candidate):
                palindromes.add(candidate)
        length += 1
    return palindromes