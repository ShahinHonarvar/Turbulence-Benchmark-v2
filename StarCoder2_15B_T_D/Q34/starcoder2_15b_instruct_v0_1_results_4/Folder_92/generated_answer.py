def find_original_set(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8):
    all_elements = set()
    for arg in [arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8]:
        all_elements |= arg
    return all_elements