def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    subset = s[106:281]
    palindromes = set()
    for start in range(len(subset)):
        for end in range(start + 136, start + 152):
            if end <= len(subset):
                candidate = subset[start:end]
                if candidate.isalpha() and is_palindrome(candidate):
                    palindromes.add(candidate)
    return palindromes