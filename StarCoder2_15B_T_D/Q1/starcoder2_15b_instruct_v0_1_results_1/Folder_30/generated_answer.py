def all_ints_inclusive(my_list):
    assert isinstance(my_list, list)
    assert all((isinstance(x, int) for x in my_list))
    return my_list[59:98]