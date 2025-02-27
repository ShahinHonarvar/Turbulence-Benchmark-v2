def return_n_greatest_chars(chars):
    if len(chars) > 10:
        chars = chars[:10]
    return sorted([char for char in chars], reverse=True)