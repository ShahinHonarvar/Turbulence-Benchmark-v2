def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    relevant_section = s[33:86]
    palindromes = set()
    for length in range(26, 32):
        for i in range(len(relevant_section) - length + 1):
            candidate = relevant_section[i:i + length]
            if candidate.isalpha() and is_palindrome(candidate):
                palindromes.add(candidate.lower())
    return palindromes