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
    flag = 0
    result = [
        [0]*20
    ]
    temp = [0];column_count = 0;row_count = 0
    while row_count < len(sample) and column_count < len(sample[0]):
        if len(temp) == (len(sample[0])-1):
            temp.append(0);assert len(temp) == 20,"Len of temp is not enough"
            row_count += 1;column_count = 0
            result.append(temp.copy());temp.clear()
        elif row_count == len(sample)-1: temp = sample[0];result.append(temp);break
        for i in range(len(window)):
            for j in range(len(window[i])):
                # print("Flag iter: ",flag)
                if window[i][j] == 1 and (j+column_count < len(sample[0])) and (i+row_count < len(sample)):
                    if sample[i+row_count][j+column_count] == window[i][j]: flag += 1
                    if i == len(window)-1 and flag == 4:flag = 0;temp.append(1);break
                    elif i == len(window)-1 and flag != 4:flag = 0;temp.append(0);break
        column_count += 1
    return result

ers = erosion(window1, sample_data)
for e in ers: print(e)