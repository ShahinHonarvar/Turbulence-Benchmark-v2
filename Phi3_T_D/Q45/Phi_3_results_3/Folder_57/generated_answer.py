def is_palindrome(s):
    return s.lower() == s[::-1].lower()

def palindromes_between_indices(text):
    characters = sorted(set(text[2:6].lower()))
    if len(characters) < 5:
        return set()

    def generate_permutations(chars, length, current, results):
        if len(current) == length and is_palindrome(current):
            results.add(current)
            return
        for i in range(len(chars)):
            char = chars[i]
            new_chars = chars[:i] + chars[i + 1:]
            generate_permutations(new_chars, length, current + char, results)
    results = set()
    generate_permutations(characters, 5, '', results)
    return results