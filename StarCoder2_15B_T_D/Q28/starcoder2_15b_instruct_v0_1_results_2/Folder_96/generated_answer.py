def return_nth_smallest_ascii(string: str) -> str:
    characters = string[:18]
    sorted_characters = sorted(characters)
    return sorted_characters[17]