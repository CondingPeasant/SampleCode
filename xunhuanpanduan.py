def Callatz(n):
    count = 0

    while n != 1:
        # if n > 1000:
            # print("error")
        if n % 2 ==0:
            n /= 2
            # print(n)
        else:
            n = (3*n+1) / 2
            # print(n)
        count = count + 1
    return count

def main():
    n = int(input())
    print(Callatz(n))

if __name__ == "__main__":
    main()












