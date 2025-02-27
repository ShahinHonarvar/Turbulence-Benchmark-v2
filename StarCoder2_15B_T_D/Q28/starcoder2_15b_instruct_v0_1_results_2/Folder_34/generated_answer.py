def return_nth_smallest_ascii(string: str) -> str:
    sorted_chars = sorted(string)
    for index, character in enumerate(sorted_chars):
        if index == 18:
            return character