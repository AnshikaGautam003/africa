    def test(n):
    if(n==0):
        return
    test(n-1)
    print(n)

test(10)