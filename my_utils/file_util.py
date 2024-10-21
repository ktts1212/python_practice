def print_file_info(file_name):
    try:
        f = open(file_name, "r", encoding="UTF-8")
    except:
        print("文件不存在")
        f = open(file_name, "w", encoding="UTF-8")
    else:
        for x in f.readlines():
            newStr = x.replace("\n", "")
            print(newStr)
    finally:
        f.close()


def append_to_file(file_name, data):
    try:
        f = open(file_name, "a", encoding="UTF-8")
    except:
        print("文件不存在")
        f = open(file_name, "w", encoding="UTF-8")
    else:
        f.write(data)
    finally:
        f.close()


if __name__ == '__main__':
    pass
