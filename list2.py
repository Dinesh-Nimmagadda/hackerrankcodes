if __name__ == '__main__':
    N = int(input())
    arr = []
    for i in range(0,N):
        comands = input().split()
        if comands[0] == "print":
            print(arr)
        elif comands[0] == "insert":
            arr.insert(int(comands[1]),int(comands[2]))
        elif comands[0] == "remove":
            arr.remove(int(comands[1]))
        elif comands[0] == "pop":
            arr.pop()
        elif comands[0] == "append":
            arr.append(int(comands[1]))
        elif comands[0] == "sort":
            arr.sort()
        else:
            arr.reverse()
