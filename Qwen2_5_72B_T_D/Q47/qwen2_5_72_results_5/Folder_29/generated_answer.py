def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    result = set()
    for start in range(15, 95):
        for end in range(start + 18, min(95, start + 74)):
            substring = s[start:end]
            if substring.isalpha() and is_palindrome(substring):
                result.add(substring.lower())
    return result