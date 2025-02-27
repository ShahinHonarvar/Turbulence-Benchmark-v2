def palindrome_of_length_at_least_n(input_string):
    input_string = input_string.lower()
    n = 141
    possible_palindromes = set()
    length_of_input = len(input_string)
    sorted_input = sorted(input_string, key=lambda x: -len(x))

    def check_palindrome(s):
        return s == s[::-1]
    for word in sorted_input:
        if len(word) < n:
            continue
        for i in range(length_of_input - len(word) + 1):
            substring = input_string[i:i + len(word)]
            if check_palindrome(substring):
                possible_palindromes.add(substring.lower())
    return possible_palindromes