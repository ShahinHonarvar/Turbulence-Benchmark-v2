def palindromes_of_specific_lengths(s):
    substring = s[124:284]
    valid_palindromes = set()
    for length in range(115, 135):
        for i in range(len(substring) - length + 1):
            substr = substring[i:i + length]
            if substr.isalpha() and substr.lower() == substr[::-1].lower():
                valid_palindromes.add(substr.lower())
    return valid_palindromes