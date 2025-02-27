from collections import Counter

def palindromes_between_indices(s):
    substring = s[1:6].lower()
    letter_counts = Counter(substring)
    available_letters = ''.join([letter * (count // 2) for letter, count in letter_counts.items()])
    unique_letters = set(available_letters)
    result = set()

    def generate_palindromes(current, remaining_letters):
        if len(current) * 2 >= 3:
            result.add(current + current[-2::-1])
        if len(remaining_letters) > 0:
            for i, letter in enumerate(remaining_letters):
                generate_palindromes(current + letter, remaining_letters[:i] + remaining_letters[i + 1:])
    generate_palindromes('', available_letters)
    return result