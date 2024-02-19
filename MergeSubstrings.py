def merge_the_tools(string, k):
    i = 0
    while(i < len(string)):
        print(''.join(list(set(string[i:i+k]))))
        i += k
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)