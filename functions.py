FILEPATH = "todos.txt"


def files_handle(m, v, f=FILEPATH):
    """ Read a text file and return the list of todos items
    or Write the to-do items in the text file
    following is structure of arguments:
    f is file path default file is 'files/todos.txt'
    m is "r" read or "w" write
    v is variable
    """
    if m == "r":
        with open(f, m) as file_to_read:
            todos_local = file_to_read.readlines()
        return todos_local
    else:
        with open(f, m) as file_to_write:
            file_to_write.writelines(v)


def parse(cal):
    parts = cal.split(" ")
    feet = float(parts[0])
    inch = float(parts[1])
    meters = feet * 0.3048 + inch * 0.0254
    return {"feet": feet, "inch": inch, "meters": meters}


if __name__ != "functions":
    print("Hello")
    print(files_handle("r", '', f="todos.txt"))
    print(parse("3.05559 2.6669"))
