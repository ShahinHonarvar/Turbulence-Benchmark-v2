def palindrome_of_length_n(s):
    n = 20

    def is_palindrome(word):
        return word.lower() == word[::-1].lower()
    palindromes = set()
    s_lower = s.lower()
    for i in range(len(s) - n + 1):
        if is_palindrome(s_lower[i:i + n]):
            palindromes.add(s_lower[i:i + n])
    return palindromes