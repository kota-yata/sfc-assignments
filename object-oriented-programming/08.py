days = [ 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ]
month = int( input( "月を入力してください：" ) )
day = int( input( "日を入力してください：" ) )

totalday = day
for m in range( month - 1 ):
    totalday += days[m]
print( f"{month}月{day}日は、1月1日から数えて、{totalday}日目です。" )
