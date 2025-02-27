def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    valid_palindromes = set()
    start, end = (106, 280)
    min_len, max_len = (136, 151)
    for i in range(start, end + 1):
        for j in range(i + min_len, min(i + max_len + 1, end + 2)):
            substring = s[i:j]
            if substring.isalpha() and is_palindrome(substring):
                valid_palindromes.add(substring)
    return valid_palindromes