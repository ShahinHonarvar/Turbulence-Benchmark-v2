def palindrome_of_length_n(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()

    def valid_palindromes(substring_len, s):
        return {s[i:i + substring_len] for i in range(len(s) - substring_len + 1) if is_palindrome(s[i:i + substring_len])}
    return valid_palindromes(21, s)