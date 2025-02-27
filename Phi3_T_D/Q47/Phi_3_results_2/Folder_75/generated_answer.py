def palindromes_of_specific_lengths(s):
    substring = s[31:75]
    palindromes = set()

    def is_palindrome(word):
        return word.lower() == word[::-1].lower()

    def generate_palindromes(start, length, current_str):
        if length == 0:
            if len(current_str) >= 23 and len(current_str) <= 39 and all((c.isalpha() for c in current_str)):
                palindromes.add(current_str)
            return
        end = start + length
        for i in range(start, end):
            if substring[i].isalpha():
                generate_palindromes(i + 1, length - 2, current_str + substring[i] + substring[i + length - 1])
    for length in range(1, min(len(substring), 39) - 1):
        generate_palindromes(0, length, '')
    return palindromes