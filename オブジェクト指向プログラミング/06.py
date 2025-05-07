nlist = [ 43, 56, 27, 36, 78, 12, 8, 93, 81, 64  ]

for n in nlist:
    match n:
        case x if round(n ** (1/3)) ** 3 == n:
            print( f"{x}は3乗の数です" )
        case x if x % 2 == 0:
            print( f"{x}は偶数です" )
        case x:
            print( f"{x}は奇数です" )
