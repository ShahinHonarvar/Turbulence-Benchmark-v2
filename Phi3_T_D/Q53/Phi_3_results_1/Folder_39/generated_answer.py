from collections import defaultdict

def palindrome_of_length_at_least_n(text):

    def is_pal_centre(start, end, length):
        while start < end:
            if text[start].lower() != text[end].lower():
                return False
            start, end = (start + 1, end - 1)
        return True
    palindromes = set()
    char_index = defaultdict(set)
    for index, char in enumerate(text):
        if char.isalpha():
            char_index[char.lower()].add(index)
    for char, positions in char_index.items():
        for pos1 in positions:
            length = max_possible_length(positions, pos1, text)
            if length >= 69:
                centers = find_pal_centres(positions, pos1, text, length)
                for center in centers:
                    palindrome = text[center - length // 2:center + length // 2 + 1].lower()
                    if len(palindrome) >= 69 and len(palindrome) == length:
                        palindromes.add(palindrome)
    return palindromes

def max_possible_length(positions, pos1, text):
    left, right = (pos1, pos1)
    while left - 1 in positions and right + 1 in positions:
        left, right = (left - 1, right + 1)
    return right - left + 1

def find_pal_centres(positions, pos1, text, length):
    left, right = (pos1, pos1)
    start_from, end_to = (left // 2, (right + length) // 2)
    pal_centres = []
    while start_from >= 0 and end_to < length:
        if text[start_from] == text[end_to]:
            pal_centres.append(positions[text[start_from].lower()].pop())
        else:
            break
        start_from, end_to = (start_from - 1, end_to + 1)
    return pal_centres