from collections import defaultdict

def palindromes_of_specific_lengths(input_string):

    def is_palindrome(s):
        return s == s[::-1]
    substring = input_string[:5].lower()
    letter_counts = defaultdict(int)
    palindromes = set()
    for char in substring:
        if char.isalpha():
            letter_counts[char] += 1
    for char, count in letter_counts.items():
        if count >= 1:
            palindromes.add(char)
        if count >= 2:
            middle = ''.join((char for _ in range(count // 2)))
            palindromes.add(middle + char + middle.lower())
        if count >= 3:
            middle = ''.join((char for _ in range((count + 1) // 2 - 1)))
            palindromes.add(middle + char + middle.lower()[::-1])
    return palindromes