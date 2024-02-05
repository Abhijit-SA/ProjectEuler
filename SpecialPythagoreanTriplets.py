# find pythagorean triplet for a+b+c = 1000


def find_triplet(n):
    for a in range(1, 1000):
        for b in range(a, 1000):
            c = (a * a + b * b) ** 0.5
            if c.is_integer() and a + b + int(c) == 1000:
                return a, b, int(c)
    return None

if __name__=="__main__":
    triplet=find_triplet(1000)
    print(triplet[0] * triplet[1] * triplet[2])
