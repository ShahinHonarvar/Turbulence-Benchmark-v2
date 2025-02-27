from collections import Counter

def palindromes_between_indices(s):
    substring = s[2:5].lower()
    counter = Counter(substring)
    palindromes = set()
    letters = [char for char, count in counter.items() if count > 0]

    def generate_palindrome(length, path='', remaining=counter.copy()):
        if length == 0:
            palindromes.add(path)
            return
        for char in letters:
            if remaining[char] > 0:
                remaining[char] -= 1
                generate_palindrome(length - 1, char + path + char, remaining)
                remaining[char] += 1
    for length in range(3, 6, 2):
        generate_palindrome(length)
    return palindromes