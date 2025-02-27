def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    return {s[i:i + length] for length in range(26, 34) for i in range(65, 100) if i + length <= 100 and is_palindrome(s[i:i + length])}