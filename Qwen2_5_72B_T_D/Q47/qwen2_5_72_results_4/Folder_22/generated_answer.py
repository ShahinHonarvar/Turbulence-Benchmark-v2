def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    valid_palindromes = set()
    s = s[100:201]
    for i in range(len(s)):
        for length in range(5, 11):
            if i + length <= len(s):
                sub = s[i:i + length]
                if sub.isalpha() and is_palindrome(sub):
                    valid_palindromes.add(sub)
    return valid_palindromes