

def max_profit(price):
    no_of_ele = len(price)
    n = no_of_ele
    profit_arr = []
    for i in xrange(no_of_ele):
        profit_arr.append(0)
    max_price = price[n-1]
    i = n - 2
    while( i >= 0):
        if(price[i] > max_price):
            max_price = price[i]
        profit_arr[i] = max(profit_arr[i+1], max_price-price[i])
        print("Profit Array:",profit_arr)
        i -= 1
    min_price = price[0]
    i = 1
    while ( i < n):
        if( price[i] < min_price):
            min_price = price[i]
        profit_arr[i] = max(profit_arr[i-1], profit_arr[i] + ( price[i] - min_price))
        print("Profit Array:",profit_arr)
        i += 1
    profit = profit_arr[n-1]
    print("Profit:",profit)



max_profit([1,2,3,4])
max_profit([1,2,3,4,10,100])
max_profit([1,100,1,100])