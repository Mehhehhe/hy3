sample_data = [
    [0]*20,
    [0]*20,
    [0,0,0,0,1,1,1,1,1,1,1,1,1,0,0,0,1,0,0,0], #3
    [0,0,0,0,1,1,1,1,1,1,1,1,1,0,0,0,1,0,0,0], #4
    [0,0,0,0,1,1,1,1,1,1,1,1,1,0,0,1,1,0,0,0], #5
    [0,0,0,0,1,1,0,0,0,1,1,1,1,0,0,1,1,0,0,0], #6
    [0,0,0,0,1,1,0,0,0,1,1,1,1,1,1,1,1,0,0,0], #7
    [0,0,0,0,1,1,0,0,0,1,1,1,1,1,1,1,0,0,0,0], #8
    [0,0,0,0,1,1,0,0,0,1,1,1,1,1,1,1,0,0,0,0], #9
    [0,0,0,0,1,1,0,0,0,1,1,1,1,1,1,1,0,0,0,0], #10
    [0,0,0,0,1,1,0,0,0,1,1,1,1,0,0,1,1,0,0,0], #11
    [0,0,0,0,1,1,1,1,1,1,1,1,1,0,0,1,1,0,0,0], #12
    [0,0,0,0,1,1,1,1,1,1,1,1,1,0,0,1,1,0,0,0], #13
    [0,0,0,0,1,1,1,1,1,1,1,1,1,0,0,0,1,0,0,0], #14
    [0]*20 
]

window1 = [
    [0,1,0],
    [1,0,1],
    [0,1,0]
]

window2 = [
    [1,1,0],
    [0]*3,
    [0]*3
]

# Checking shape
# for i in sample_data:
#     print(i, end='\n')

def erosion(window, sample):
    # Setup
    flag = 0;z_flag=0
    result = [[0]*20]
    temp = [];column_count = 0;row_count = 0;total_one=0;total_zero=0

    for i in window:
        for j in i:
            if j==1: total_one+=1
            else:total_zero+=1

    # Process: until row is equal to actual length of nested list
    while row_count <= len(sample):
        # Check if moving window aka structure element is hit the corner (last column) 
        if column_count == (len(sample[0])):
            # Append zero to complete a list (3x3 corner is 0), reset column counter 
            # and move window to next row
            temp.append(0);row_count += 1;column_count = 0
            # Copy from temp and append into result then clear all values in temp.
            result.append(temp.copy());temp.clear()
            # If hit the last row, append all zeroes and break a while
            # or continue the loop
            if row_count == len(sample)-2: result.append([0]*20);break
            else:continue
        
        # Member appending process
        sliced_list = [
            sample[row_count][column_count:column_count+len(window)],
            sample[row_count+1][column_count:column_count+len(window)],
            sample[row_count+2][column_count:column_count+len(window)],
        ]

        for row_index, row_value in enumerate(sliced_list):
            for col_index, col_value in enumerate(row_value):
                if window[row_index][col_index] == col_value and col_value == 1:
                    flag += 1
                    if flag == total_one:temp.append(1);flag=0;z_flag=0;break
                else:
                    z_flag-=1
        if z_flag < -total_zero:temp.append(0);z_flag=0;flag=0
        column_count += 1;sliced_list.clear()
    return result

ers = erosion(window1, sample_data);print(len(ers))
for e in ers: print(e)