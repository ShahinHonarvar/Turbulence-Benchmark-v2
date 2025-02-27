def palindromes_of_specific_lengths(s):
    s = s[40:90].lower()
    palindromes = set()

    def is_palindrome(sub):
        return sub == sub[::-1]
    for length in range(23, 39):
        for i in range(len(s) - length + 1):
            if s[i:i + length].isalpha():
                if is_palindrome(s[i:i + length]):
                    palindromes.add(s[i:i + length])
    return palindromes