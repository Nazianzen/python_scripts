
try:
    f = open('test_copy.txt')
    if f.name == 'test_copy.txt':
        raise Exception
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print('Error!')
else:
    print(f.read())
    f.close()
finally:
    print("Executing finally...")
