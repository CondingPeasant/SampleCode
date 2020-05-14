def Callatz(n):
    result = [n]

    while n != 1:
        # if n > 1000:
            # print("error")
        if n % 2 ==0:
            n /= 2
            # print(n)
        else:
            n = (3*n+1) / 2
            # print(n)
        result.append(int(n))
    return result

def main():
    n = int(input())
    print(Callatz(n))

if __name__ == "__main__":
    main()












