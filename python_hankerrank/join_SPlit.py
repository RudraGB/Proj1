def split_and_join(line):
    s_line = line.split(" ")
    line = "-".join(s_line)
    return line

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)