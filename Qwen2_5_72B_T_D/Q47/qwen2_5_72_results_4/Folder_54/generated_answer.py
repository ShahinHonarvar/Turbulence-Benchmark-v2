def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    s = s[27:78]
    palindromes = set()
    for start in range(len(s)):
        for end in range(start + 17, start + 20):
            if end <= len(s):
                candidate = s[start:end]
                if candidate.isalpha() and is_palindrome(candidate):
                    palindromes.add(candidate)
    return palindromes