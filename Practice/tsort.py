def tsort():
    n = []
    for i in range(int(input("Enter the number of test cases: "))):
        n.append(int(input()))
    print("Sorted list:")
    for i in range(len(n)):
        for j in range(i+1, len(n)):
            if n[i] > n[j]:
                n[i], n[j] = n[j], n[i]

    print(n)

tsort()
