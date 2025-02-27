def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    valid_palindromes = set()
    substring = s[1:9]
    for i in range(1, len(substring) + 1):
        for j in range(i):
            current = substring[j:i]
            if 3 <= len(current) <= 4 and current.isalpha() and is_palindrome(current):
                valid_palindromes.add(current.lower())
    return valid_palindromes