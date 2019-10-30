# File objects

with open('giddy.jpg', 'rb') as rf:
    with open('giddy_copy.jpg', 'wb') as wf:
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)

# with open('test2.txt', 'w') as f:
#     f.write('Test')
#     f.seek(0)
#     f.write('test')

# with open('test.txt', 'r') as f:
#
#     size_to_read = 5
#
#     f_contents = f.read(size_to_read)
#     print(f_contents, end='')
#
#     f.seek(3)
#
#     f_contents = f.read(size_to_read)
#     print(f_contents, end='')

#    print(f.tell())

#    while len(f_contents) > 0:
#        print(f_contents, end='*')
#        f_contents = f.read(size_to_read)

#        for line in f:
#            print(line, end='')

#        f_contents = f.readline()
#        print(f_contents, end='')


# f = open('test.txt', 'r')

# print(f.read())

# f.close
