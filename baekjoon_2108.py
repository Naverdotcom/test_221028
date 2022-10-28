## 값 입력
N = int( input( ) )
input_dict = { i : 0 for i in range( -4000, 4001 ) }
result_arr = [ ]

## 빈도 딕셔너리와 정렬된 리스트 생성
for i in range( N ):
    input_dict[ int( input( ) ) ] += 1

for i in input_dict.keys( ):
    for _ in range( input_dict[ i ] ):
        result_arr.append( i )

## 결과 계산과 출력
mean = round( sum( result_arr ) / N )
median = result_arr[ N // 2 ]
mode_value = max( input_dict.values( ) )
mode = [ key[ 0 ] for key in input_dict.items( ) if key[ 1 ] == mode_value ]
value_range = result_arr[ -1 ] - result_arr[ 0 ]

print( mean )
print( median )
print( mode[ 1 ] if len( mode ) >= 2 else mode[ 0 ] )
print( value_range )