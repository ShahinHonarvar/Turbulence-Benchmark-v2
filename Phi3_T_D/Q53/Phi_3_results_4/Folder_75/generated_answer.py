def palindrome_of_length_at_least_n(s):

    def is_palindrome(word):
        return word == word[::-1]
    unique_chars = set(s.lower())
    if len(unique_chars) > 26:
        return set()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 40, len(s) + 1):
            if len(set(s[i:j].lower())) <= 26:
                substring = s[i:j]
                if is_palindrome(substring):
                    palindromes.add(substring)
    return palindromes