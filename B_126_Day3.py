# Each question is attached here. 1 is uncommented, the rest two are commented out.

# 1
def longEven(s):
    l = list(filter(lambda x: len(x)%2 == 0, s.split()))
    word,m = l[0],len(l[0])
    for w in l[1:]:
        if len(w) > m:
            m = len(w)
            word = w
        else:
            continue
    return word

if __name__ == "__main__":
    test_string = input()
    res = longEven(test_string)
    print(res)

'''# (a)
def nEven(s,n):
    l = list(filter(lambda x: len(x)%2 == 0, s.split()))
    return l[n-1]

if __name__ == "__main__":
    test_string = input()
    n = int(input())
    res = nEven(test_string,n)
    print(res)
'''

'''# (b)
def mthEven(s,m):
    l = list(filter(lambda x: len(x)%2 == 0, s.split()))
    lens = sorted(list(set([len(x) for x in l])),reverse=True)
    final_length = lens[m-1]
    return " ".join(list(filter(lambda x: len(x) == final_length,l)))

if __name__ == "__main__":
    test_string = input()
    m = int(input())
    res = mthEven(test_string,m)
    print(res)
'''
