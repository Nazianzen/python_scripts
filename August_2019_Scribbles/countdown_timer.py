import time

# def countdown(t):
#     i = 0
#     while i <= t:
#         print('{}...'.format(t), end='\r')
#         time.sleep(1)
#         t -= 1

# countdown(3)

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        t -= 1
    print('Goodbye!')

countdown(10)

# def countdown(p,q):
#     i = p
#     j = q
#     k = 0
#     while True:
#         if (j == -1):
#             j = 59
#             i -= 1
#         if (j > 9):
#             print(str(k) + str(i) + ':'+ str(j), end='\r')
#         else:
#             print(str(k) + str(i) + ':' + str(k) + str(j), end = '\r')
#         time.sleep(1)
#         j -= 1
#         if (i==0 and j==-1):
#             break
#     if (i==0 and j==-1):
#         print('Goodbye!', end = '\r')
#         time.sleep(1)

# countdown(0,10)