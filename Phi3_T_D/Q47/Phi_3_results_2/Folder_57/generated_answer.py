def is_palindrome(s):
    return s == s[::-1]

def palindromes_of_specific_lengths(input_string):
    palindrome_set = set()
    for l in range(39, 53):
        for i in range(16, len(input_string) - l + 1):
            candidate = input_string[i:i + l].lower()
            if all((char.isalpha() for char in candidate)):
                if is_palindrome(candidate):
                    palindrome_set.add(candidate)
    return palindrome_set