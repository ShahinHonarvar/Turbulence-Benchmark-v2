def palindrome_of_length_at_least_n(s):
    filtered_chars = [char.lower() for char in s if char.isalpha()]
    filtered_string = ''.join(filtered_chars)
    length = len(filtered_string)
    palindromes = set()
    for i in range(length):
        for j in range(i + 137, length + 1):
            substring = filtered_string[i:j]
            reversed_substring = substring[::-1]
            if substring == reversed_substring:
                palindromes.add(substring)
    return palindromes