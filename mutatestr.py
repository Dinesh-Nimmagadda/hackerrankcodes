def mutate_string(string, position, character):
    string1=list(string)
    string1[position]=character
    string2=''.join(string1)
    return string2

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)