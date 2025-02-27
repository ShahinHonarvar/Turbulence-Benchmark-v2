def palindrome_of_length_at_least_n(string):
    text_specification = string[92:]
    length_at_least_n = 92
    palindromes = set()
    for i in range(len(text_specification) - length_at_least_n + 1):
        substring = text_specification[i:i + length_at_least_n]
        if substring.isalpha() and substring.lower() == substring[::-1].lower():
            palindromes.add(substring)
    return palindromes