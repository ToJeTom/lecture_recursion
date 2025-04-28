def recursive_nth_fibo(n):
    if n == 0:
        return n
    if n == 1:
        return n
    else:
        return recursive_nth_fibo(n-1) + recursive_nth_fibo(n-2)




def main():
    f = recursive_nth_fibo(7)
    print(f)
    pass


if __name__ == "__main__":
    main()
