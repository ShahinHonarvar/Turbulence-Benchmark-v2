from string import ascii_letters

def palindromes_of_specific_lengths(s):
    substring = s[15:95]
    valid_palindromes = set()

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower() and all((c in ascii_letters for c in sub))
    for length in range(18, 74):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if is_palindrome(candidate):
                valid_palindromes.add(candidate)
    return valid_palindromes