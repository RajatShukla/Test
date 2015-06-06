
array1 = [2,'NA',7,'NA','NA',10,'NA']
array2 = [5,8,12,14]
array1 = [1,2,3,4,5,6,'NA','NA','NA','NA']
array2 = [7,8,9,10]
j=0
for i in range(len(array1)):
    if array1[i] != 'NA':
        continue
    else:
        if ( (i+1 < len(array1)) and (array1[i+1] != 'NA')):
            if( (array1[i-1] < array2[j]) and (array2[j]< array1[i+1])):
                array1[i] = array2[j]
                j += 1
            else:
                array1[i] = array1[i+1]
                array1[i+1] =  array2[j]
                j += 1
        else:
            array1[i] = array2[j]
            j += 1

print(array1)










