def palindromes_between_indices(s):

    def is_palindrome(s):
        return s == s[::-1]
    substring = s[4:9].lower()
    unique_chars = set(substring)
    char_freq = {char: substring.count(char) for char in unique_chars}
    palindromes = set()

    def generate_palindromes(current, remaining):
        if len(current) >= 4 and is_palindrome(current):
            palindromes.add(current)
        for char in remaining:
            if remaining[char] > 1:
                remaining[char] -= 2
                generate_palindromes(char + current + char, remaining)
                remaining[char] += 2
            if len(current) % 2 == 0:
                remaining[char] -= 1
                generate_palindromes(current + char, remaining)
                remaining[char] += 1
    generate_palindromes('', char_freq)
    return palindromes