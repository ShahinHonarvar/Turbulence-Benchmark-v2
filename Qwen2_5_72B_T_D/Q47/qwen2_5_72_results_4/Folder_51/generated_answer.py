def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    substring = s[2:9]
    palindromes = set()
    for length in range(3, 5):
        for i in range(len(substring) - length + 1):
            part = substring[i:i + length]
            if is_palindrome(part) and part.isalpha():
                palindromes.add(part.lower())
    return palindromes