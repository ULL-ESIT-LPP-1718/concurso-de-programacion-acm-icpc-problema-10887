from sets import Set

def main ():
    T = int(input())
    Case = []
    while (T > 0):
        result = Set()
        A = []
        B = []
        M, N = raw_input().split()
        M, N = [int(M), int(N)]
        while (M > 0):
            A.append(raw_input())
            M -= 1
        while (N > 0):
            B.append(raw_input())
            N -= 1
        for x in A:
            for y in B:
                dummy = x + y
                result.add(dummy)
        Case.append(len(result))
        T -= 1
    for i in Case:
        print("Case " + str(Case.index(i) + 1) + ": " + str(i))
    

if __name__ == '__main__':
    main()