from collections import Counter

def palindromes_between_indices(s):
    substring = s[4:10]
    letter_counts = Counter(substring)
    palindromes = set()

    def can_form_palindrome(counts):
        odd_counts = sum((1 for count in counts.values() if count % 2 != 0))
        return odd_counts <= 1

    def generate_palindromes(counts, length):
        if length == 0:
            return {''}
        palindromes = set()
        for letter in counts:
            if counts[letter] >= 2:
                counts[letter] -= 2
                for middle in generate_palindromes(counts, length - 2):
                    palindromes.add(letter + middle + letter)
                counts[letter] += 2
        return palindromes
    if can_form_palindrome(letter_counts):
        for length in range(7, 11):
            for palindrome in generate_palindromes(letter_counts, length):
                palindromes.add(palindrome.lower())
    return palindromes