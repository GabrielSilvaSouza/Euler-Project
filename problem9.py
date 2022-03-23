def pitagoric():
    for a in range(1,1334):
        for b in range(1,334):
            for c in range(1,334):
                if a+b+c == 1000:
                    eq = b**2 + a**2
                    if c**2 == eq:
                        return (a,b,c)
        

if __name__ == '__main__':
    print(pitagoric())
