def count_substring(string, sub_string):
    
    count=0
    for var in range(len(string)):
        if string[var] == sub_string[0]:
            sub_len = len(sub_string)
            new_var = var+(sub_len)
            if string[var:new_var] == sub_string:
                count+=1
    return count

if __name__ == '__main__':