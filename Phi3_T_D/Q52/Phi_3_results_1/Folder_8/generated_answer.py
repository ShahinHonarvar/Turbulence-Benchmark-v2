def palindrome_of_length_n(input_string):
    string = input_string.lower()
    all_letter_substrings = {string[i:i + 49] for i in range(len(string) - 48)}
    palindromes = {s for s in all_letter_substrings if s == s[::-1] and s.isalpha()}
    return palindromes