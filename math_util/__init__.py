def reverseArray(array, start, end):
    if(start >= end):
        return
    temp = array[start]
    array[start] = array[end]
    array[end] = temp
    reverseArray(array, start+1, end-1)


array = [1,2,3,4,5,6,7]
#reverseArray(array,0,6)


def getMedian(arr1, arr2, n):
    i = 0
    j = 0
    count = 0
    m1, m2 = -1, -1
    for count in xrange(n+1):
        if ( i == n):
            m1 = m2
            m2 = arr2[0]
            break;
        elif ( j == n ):
            m1 = m2
            m2 = arr1[0]
            break
        if ( arr1[i] < arr2[j]):
            m1 = m2
            m2 = arr1[i]
            i += 1
        else:
            m1 = m2
            m2 = arr2[j]
            j += 1
    return ( m1 + m2)/2


#print(getMedian([1,3,5,7,9],[2,4,6,8,10],5))

def rotate_an_array(array):
    no_of_rows = len(array)
    no_of_cols = len(array[0])
    new_array = []
    m = no_of_rows - 1
    for i in range(no_of_cols):
        new_col = [0,0,0,0]
        for j in range(no_of_rows)[:no_of_rows:1]:
            a = array[j][i]
            new_col[m] = a
            m -= 1
        m = no_of_rows -1
        new_array.append(new_col)
    return new_array



array = [['*', '*', '*', '^', '*', '*', '*'],['*', '*', '*', '|', '*', '*', '*'],['*', '*', '*', '|', '*', '*', '*'],
         ['*', '*', '*', '|', '*', '*', '*']]
#print(rotate_an_array([[1,2,3,4],[5,6,7,8]]))
#print(rotate_an_array(array))


def duplicate_element_find_out(arr):
  print("The repeating elements are: \n")
  for i  in xrange(len(array)):
    if (arr[abs(arr[i])] >= 0):
      arr[abs(arr[i])] = -arr[abs(arr[i])]
    else:
      print(abs(arr[i]))

#duplicate_element_find_out([1,2,1,3,4,3,4,12,1])





def unsorted_array_finder(array):
    i = 0
    j = 1
    m = len(array) -1
    n = m - 1
    for i  in xrange(len(array)):
        if ( array[i] < array[j] ):
            i = j
            j += 1
        else:
            if( array[n] < array[m]):
                m = n
                n -= 1

    return (j-1,m)

# print(unsorted_array_finder([1,2,3,5,4,7,6,8,9,10,11,12]))
# print(unsorted_array_finder([1,2,5,4,6]))
# print(unsorted_array_finder([1,2,3,5,5,7,6,8]))
# print(unsorted_array_finder([1,2,9,5,4,7,6,8]))
# print(unsorted_array_finder([1,2,3,5,4,6,6,8]))



def segregate_even_odd_no(array):
    arr_len = len(array)
    left = 0
    right = arr_len - 1
    while(left < right):
        while(array[left]%2 == 0 & left < right):
            left += 1
        while(array[right]%2 == 1 & left < right):
            right -= 1
        if(left < right):
            temp = array[left]
            array[left] = array[right]
            array[right] = temp
            left += 1
            right -= 1
    print(array)


print(segregate_even_odd_no([1,2,3,4,5,6,7,8,9,10,11,12,13]))









