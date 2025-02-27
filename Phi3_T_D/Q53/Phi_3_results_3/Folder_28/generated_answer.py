def palindrome_of_length_at_least_n(string):
    length = len(string)
    palindromes = set()
    for start in range(length):
        for end in range(start, min(start + 42, length)):
            substring = string[start:end + 1]
            if substring.lower() == substring[::-1].lower():
                palindromes.add(substring.lower())
    return palindromes