def counter(u):
    count = 0
    for i in range(1, int(u**0.5) + 1):
        if u % i == 0:
            count += 2
            if i == u // i:
                count -= 1
    
    return count



def triangle_number(d):
    t_n = 1
    nt_number = 2

    while True:
        t_n += nt_number
        nt_number += 1

        if counter(t_n) > d:
            return t_n
        
res = triangle_number(500)
print(res)