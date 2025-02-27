def palindromes_of_specific_lengths(string):
    words = string[:5]
    palindromes = set()
    for i in range(len(words) - 2):
        substring = words[i:i + 4]
        if substring.isalpha() and 3 <= len(substring) <= 4:
            substr_lower = substring.lower()
            if substr_lower == substr_lower[::-1]:
                palindromes.add(substring)
    return palindromes