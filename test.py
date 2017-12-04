import io

f = io.open('test.txt', 'w+')
c = f.write('ccc')
print(c)
f.close()
