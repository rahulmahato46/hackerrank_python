def mutate_string(string, position, character):
    new_list=list(string)
    new_list[position] = character
    joined_str = "".join(new_list)
    return joined_str

if __name__ == '__main__':