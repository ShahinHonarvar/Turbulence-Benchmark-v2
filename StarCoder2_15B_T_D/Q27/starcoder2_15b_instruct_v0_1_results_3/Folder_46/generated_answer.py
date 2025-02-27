def insert_after_index(text):
    list = eval(text.split('list = ')[1].split('\n')[0])
    index = 28 + 1
    list.insert(index, 717.02)
    return list