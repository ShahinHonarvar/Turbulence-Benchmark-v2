def return_nth_smallest_ascii(string):
    characters = string[:12]
    characters_list = list(characters)
    characters_list.sort()
    return characters_list[11]