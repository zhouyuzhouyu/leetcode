def trim(s:str):
    if s[0] == ' ':
        s = s[1:]
    if s[-1] == ' ':
        s = s[:-1]

    return s


print(trim(' hjhjhbjhjh hjh  '))
