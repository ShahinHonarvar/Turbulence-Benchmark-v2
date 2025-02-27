def palindrome_of_length_n(s):

    def is_palindrome(substr):
        return substr.lower() == substr.lower()[::-1]
    all_palindromes = set()
    s_lower = s.lower()
    for i in range(len(s_lower) - 46):
        substring = s_lower[i:i + 47]
        if all((char.isalpha() for char in substring)):
            if is_palindrome(substring):
                all_palindromes.add(substring)
    return all_palindromes