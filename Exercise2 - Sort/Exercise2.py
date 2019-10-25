import sys
import MySort
import time

def readFile(s):
    """
    :param self:
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
                lst[i] = " "
        for i in lst:
            result = result + i

    words = result.split()
    return words

def writeFile(s,num):
    """
    :param s: filename to write
    :param num: write content
    :return:
    """
    file_name = s
    my_open = open(file_name, 'a')
    # 打开fie_name路径下的my_infor.txt文件,采用追加模式
    # 若文件不存在,创建，若存在，追加
    my_open.write(num)
    my_open.write('\n')
    my_open.close()

    ##检查是否正确追加
    my_open = open(file_name, 'r')
    # 读取file_name路径下的my_write.txt文件
    my_infor = my_open.readlines()
    my_open.close()

if __name__ == "__main__":
    sys.setrecursionlimit(20000)
    pathname = "pride-and-prejudice.txt"
    words = readFile(pathname)
    print("----------Selection Sort----------")
    print(len(words))
    # print(words)
    a = list(words)
    starttime = time.clock()
    MySort.selectionSort(a)
    endtime = time.clock()
    # print("sorted:", a)
    # print("unsorted:", words)
    filename = "selection sort.txt"
    print(endtime - starttime, "s")
    writeFile(filename, str(endtime-starttime))
    print("----------Insert Sort-------------")
    b = list(words)
    starttime2 = time.clock()
    MySort.insertSort(b)
    endtime2 = time.clock()
    # print("sorted:", b)
    # print("unsorted:", words)
    filename = "insert sort.txt"
    print(endtime - starttime, "s")
    writeFile(filename, str(endtime2 - starttime2))
    print("--------In Place Heap Sort--------")
    c = list(words)
    starttime3 = time.clock()
    MySort.in_place_HeapSort(c)
    endtime3 = time.clock()
    # print("sorted:", c)
    # print("unsorted:", words)
    filename = "in-place heap sort.txt"
    print(endtime3 - starttime3, "s")
    writeFile(filename, str(endtime3 - starttime3))
    print("------------Merge Sort------------")
    d = list(words)
    starttime4 = time.clock()
    MySort.mergeSort(d)
    endtime4 = time.clock()
    # print("sorted:", d)
    # print("unsorted:", words)
    filename = "merge sort.txt"
    print(endtime4 - starttime4, "s")
    writeFile(filename, str(endtime4 - starttime4))
    print("------------Quick Sort------------")
    e = list(words)
    starttime5 = time.clock()
    MySort.quickSort(e)
    endtime5 = time.clock()
    # print("sorted:", e)
    # print("unsorted:", words)
    filename = "quick sort.txt"
    print(endtime5 - starttime5, "s")
    writeFile(filename, str(endtime5 - starttime5))
    print("----------Are they same?----------")
    print(a==b==c==d==e)
