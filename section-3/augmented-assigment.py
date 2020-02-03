from datetime import datetime

@profile
def doStuff(way):
    if way == 'augmented':
        a = 0
        while a < 99999:
            a += 1
    else:
        a = 0
        while a < 99999:
            a = a + 1


if __name__ == '__main__':
    startTime = datetime.now()
    doStuff('augmented')
    end_date_time = datetime.now()

    #Python 3: 
    print('Augmented time: ', end_date_time - startTime)

    startTime = datetime.now()
    doStuff('normal')
    end_date_time = datetime.now()

    #Python 3: 
    print('Normal time: ', end_date_time - startTime)


