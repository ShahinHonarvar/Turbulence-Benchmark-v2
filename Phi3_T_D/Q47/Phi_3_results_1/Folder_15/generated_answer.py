def palindromes_of_specific_lengths(s):
    length = min(6, len(s[0:7]))
    s_lower = s[0:length].lower()
    palindromes = set()

    def is_valid_palindrome(sub, length):
        return all((c.isalpha() for c in sub)) and length >= 3 and (length <= 6) and (sub == sub[::-1])
    for i in range(len(s_lower)):
        for j in range(i + 3, min(i + 7, length + 1)):
            if is_valid_palindrome(s_lower[i:j], j - i):
                palindromes.add(s_lower[i:j])
    return palindromes