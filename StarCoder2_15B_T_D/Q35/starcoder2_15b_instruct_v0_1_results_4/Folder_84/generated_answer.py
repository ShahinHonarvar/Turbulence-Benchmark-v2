def remove_repeat_chars(text: str) -> str:
    character_counts = {}
    for index, character in enumerate(text):
        if character not in character_counts:
            character_counts[character] = []
        character_counts[character].append(index)
    for character, indices in character_counts.items():
        if len(indices) > 1 and 32 < indices[0] < 44:
            text = text.replace(character, '')
    return text