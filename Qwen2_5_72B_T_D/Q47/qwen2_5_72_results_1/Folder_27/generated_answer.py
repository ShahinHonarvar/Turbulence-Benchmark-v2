def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()

    def is_valid(sub):
        return sub.isalpha() and 26 <= len(sub) <= 29
    s = s[13:100]
    found_palindromes = set()
    for start in range(len(s)):
        for end in range(start + 26, min(len(s) + 1, start + 30)):
            substr = s[start:end]
            if is_palindrome(substr) and is_valid(substr):
                found_palindromes.add(substr)
    return found_palindromes