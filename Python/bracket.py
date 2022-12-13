def check_brackets(string):
    if len(string) % 2 == 1:
        return False
    brackets = ('(', ')', '{', '}', '[', ']')
    list_string = list(string)
    for b in brackets[::2]:
        while b in list_string:
            if brackets[brackets.index(b) + 1] in list_string[list_string.index(b): len(list_string)]:
                list_string.remove(b)
                list_string.remove(brackets[brackets.index(b) + 1])
            else:
                return False 
    return True

                
                    
        

print(check_brackets('({)}'))