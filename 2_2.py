def chisla(number):
    number = number.split()
    b = ''
    for n in range(len(number)):
        number[n] = int(number[n])
        number[n] = bin(number[n])
        b = b + str(number[n]) + ' '
    return (b.replace('0b',''))
