def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    substring = s[13:96]
    found_palindromes = set()
    for length in range(57, 61):
        for start in range(len(substring) - length + 1):
            part = substring[start:start + length]
            if is_palindrome(part) and part.isalpha():
                found_palindromes.add(part)
    return found_palindromes