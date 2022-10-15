def chisla(n):
    edenici = {1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять', 6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять'}
    desyatki = {10: 'десять', 20: 'двадцать', 30: 'тридцать', 40: 'сорок', 50: 'пятьдесят', 60: 'шестьдесят', 70: 'семьдесят', 80: 'восемьдесят', 90: 'девяносто'}
    isklyucheniya = {11: 'одиннадцать', 12: 'двенадцать', 13: 'тринадцать', 14: 'четырнадцать', 15: 'пятнадцать', 16: 'шестнадцать', 17: 'семнадцать', 18: 'восемнадцать', 19: 'девятнадцать'}
    n1 = n % 10
    n2 = n - n1
    if n < 99 and n > 1:
        if n < 10:
            return edenici.get(n)
        elif 10 < n < 20:
            return isklyucheniya.get(n)
        elif n >= 10 and n in desyatki:
            return desyatki.get(n)
        else:
            return desyatki.get(n2) + ' ' + edenici.get(n1)
    if n > 99:
        return 'много'
    if n < 1:
        return None
def verblydu(n):
    ch = chisla(n)
    v1 ='верблюд'
    v2 ='верблюда'
    v3 ='верблюдов'
    if n%10 == 1 and n!=11:
        i1 = 'В караване был {} {}'.format(ch, v1)
        return (i1)
    elif (n%10 == 2 or n%10 == 3 or n%10 == 4) and n != 14 and n != 12 and n != 13:
        i2 = 'В караване было {} {}'.format(ch, v2)
        return (i2)
    else:
        i3 = 'В караване было {} {}'.format(ch, v3)
        return (i3)