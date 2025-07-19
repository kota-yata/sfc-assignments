base = int( input( "何進数ですか：" ) )
strvalue = input( f"{base}進数の文字列を入力してください：" )
digits = "0123456789abcdefghijklmnopqrstuvwxyz"

result = 0
for n in list( strvalue ):
    for m in range(len(digits)):
        if n == digits[m]:
            result = result * base + m
            break
print( result, int( strvalue, base ) )