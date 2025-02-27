def return_nth_smallest_ascii(string: str) -> str:
    characters = list(string)
    sublist = characters[17:66]
    sorted_sublist = sorted(sublist)
    return sorted_sublist[7]