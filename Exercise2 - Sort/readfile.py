def readFile(s):
    """
    :param s: pathname "test.txt"
    :return: list of words in the file
    """
    filename = s
    result = ""
    fhand = open(filename)
    for line in fhand:
        lst = list(line)
        for i in range(len(lst)):
            if (not lst[i].isalnum() and lst[i] != " "):
                lst[i] = ""
        for i in lst:
            result = result + i

    words = result.split()
    return words
    #print(words)