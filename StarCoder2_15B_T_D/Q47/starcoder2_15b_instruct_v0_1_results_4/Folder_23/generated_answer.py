def palindromes_of_specific_lengths(string):
    substring = string[23:95]
    palindromes = []
    for length in range(17, 56):
        for start in range(len(substring) - length + 1):
            window = substring[start:start + length]
            if window == window[::-1]:
                palindromes.append(window)
    filtered_palindromes = []
    for palindrome in palindromes:
        if all((ch.isalpha() for ch in palindrome)):
            filtered_palindromes.append(palindrome)
    return set(filtered_palindromes)