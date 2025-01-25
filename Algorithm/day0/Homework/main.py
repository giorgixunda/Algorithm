# პირველი დავალება
def count(a,b,c):
    result = (b // c) - ((a - 1) // c)
    return result

print(count(30,60,20))
# მეორე დავალება
def count_conveter(a,b):
    arr = []
    while a > 0:
        res = a % b
        if res == 10:
            arr.append("A")
        elif res == 11:
            arr.append("B")
        elif res == 12:
            arr.append("C")
        elif res == 13:
            arr.append("D")
        elif res == 14:
            arr.append("E")
        elif res == 15:
            arr.append("F")
        else:                
            arr.append(str(res))
            print(a)
        a = a // b
    return "".join(arr)    
print(count_conveter(2,2))
print(count_conveter(2,4))
print(count_conveter(2,10))
print(count_conveter(31,16))
# მესამე დავალება
def findnumber(a,b,c,d,e):
    if a > b:
        if a > c:
            if a > d:
                if a > e:
                    return a
                else:
                    return e
    elif b > c:
        if b > d:
            if b > e:
                return b
            else:
                return e
    elif c > d:
        if c > e:
            return c
        else:
            return e
    elif d > e:
        return d
    else:
        return e

                                        
print(findnumber(30,33,36,42,42))