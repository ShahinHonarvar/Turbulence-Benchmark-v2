def palindromes_of_specific_lengths(string):
    substring = string[200:301]
    palindromes = set()
    for i in range(len(substring) - 10):
        for j in range(10, 51):
            if i + j > len(substring):
                break
            potential_palindrome = substring[i:i + j]
            if potential_palindrome.lower() == potential_palindrome[::-1].lower():
                palindromes.add(potential_palindrome)
    return palindromes