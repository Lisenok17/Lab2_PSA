def GRINVICH(now='2022-09-18 12:41:18-03:00'):
        date = now.split()[0].split('-')
        temp = now.split()[1]
        if '+' in temp:
            time = now.split()[1].split('+')[0].split(':')
            tz = ['+'] + now.split()[1].split('+')[1].split(':')
        elif '-' in temp:
            time = now.split()[1].split('-')[0].split(':')
            tz = ['-'] + now.split()[1].split('-')[1].split(':')
        return date, time, tz
print(GRINVICH())
