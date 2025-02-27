def palindrome_of_length_at_least_n(s):
    extracted_palindromes = set()
    s_lower = s.lower()

    def is_palindrome(candidate):
        return candidate == candidate[::-1]
    for i in range(len(s_lower)):
        for j in range(i + 45, len(s_lower)):
            if all((c.isalpha() for c in s_lower[i:j + 1])) and is_palindrome(s_lower[i:j + 1]):
                extracted_palindromes.add(s_lower[i:j + 1])
    return extracted_palindromes