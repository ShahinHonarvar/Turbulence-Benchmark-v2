def is_palindrome(s):
    return s.lower() == s[::-1].lower()

def char_combinations(length, characters):
    if length == 0:
        yield ''
    else:
        for char in sorted(characters, key=lambda c: (-characters.count(c), -ord(c))):
            for combo in char_combinations(length - 1, characters.replace(char, '', 1)):
                yield (char + combo)

def palindromes_between_indices(s):
    subset = s[3:6].lower()
    unique_chars = ''.join(sorted(subset, key=lambda c: (-subset.count(c), -ord(c))))
    palindromes = {combo for combo in char_combinations(len(unique_chars), unique_chars) if is_palindrome(combo)}
    return {p for p in palindromes if len(p) >= 3}