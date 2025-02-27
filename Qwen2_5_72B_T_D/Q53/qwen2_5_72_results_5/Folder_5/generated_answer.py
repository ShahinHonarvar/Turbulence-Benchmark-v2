def palindrome_of_length_at_least_n(text):
    text_lower = text.lower()
    palindromes = set()
    n = len(text)

    def is_valid_palindrome(sub):
        return sub == sub[::-1] and sub.isalpha()
    for i in range(n):
        for j in range(i + 45, n):
            substring = text_lower[i:j + 1]
            if is_valid_palindrome(substring):
                palindromes.add(text[i:j + 1])
    return palindromes