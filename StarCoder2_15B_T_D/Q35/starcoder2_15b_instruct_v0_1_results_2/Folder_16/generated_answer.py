from collections import Counter

def remove_repeat_chars(string: str) -> str:
    counter = Counter(string)
    indices_to_remove = {index for index, char in enumerate(string) if counter[char] > 1 and 90 <= index < 97}
    result = [char for index, char in enumerate(string) if index not in indices_to_remove]
    return ''.join(result)