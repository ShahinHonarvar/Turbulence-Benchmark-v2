from collections import Counter

def palindromes_between_indices(s):
    substring = s[2:9].lower()
    letter_count = Counter(substring)
    even_letters = [char for char, count in letter_count.items() if count % 2 == 0 and char.isalpha()]
    odd_letters = [char for char, count in letter_count.items() if count % 2 != 0 and char.isalpha()]
    if len(even_letters) + len(odd_letters) < 2:
        return set()

    def generate_palindromes(available_chars, min_length):
        if len(available_chars) == 0:
            return set([''])
        middle = [char for char, count in available_chars.items() if count % 2 != 0]
        if len(middle) == 0:
            middle.append('')
        available_chars = {char: count // 2 for char, count in available_chars.items()}

        def helper(path):
            if not available_chars:
                return [path + m + path[::-1]]
            results = []
            for char in list(available_chars.keys()):
                available_chars[char] -= 1
                if available_chars[char] == 0:
                    del available_chars[char]
                results.extend(helper(path + char))
                available_chars[char] = 1 + available_chars.get(char, 0)
            return results
        return set((p for p in helper('') if len(p) >= min_length and p == p[::-1]))
    available_chars = {char: letter_count[char] for char in even_letters + odd_letters}
    return generate_palindromes(available_chars, 4)