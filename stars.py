def rectangle_star(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print("*", end=" ")
        print("")

rectangle_star(5)
