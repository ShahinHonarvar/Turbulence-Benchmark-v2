def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[119:257]
    for length in range(104, 124):
        for i in range(len(substring) - length + 1):
            potential_palindrome = substring[i:i + length]
            if potential_palindrome.lower() == potential_palindrome[::-1].lower() and potential_palindrome.isalpha():
                result.add(potential_palindrome.lower())
    return result