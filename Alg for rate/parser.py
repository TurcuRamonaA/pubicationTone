file = open('/home/training/Desktop/ToneChecker/data.txt','r')
file2 = open('/home/training/Desktop/ToneChecker/output.txt', 'w')


cuvinte=file.read().split()

ok=0
i=0
while i<cuvinte.__len__():
    if cuvinte[i]=='<conclusion>':
        i=i+1
        ok = 1
    if ok==1:
        if cuvinte[i]!='</conclusion>':
            print(cuvinte[i])
            file2.write(cuvinte[i]+'\n')

        elif cuvinte[i]=='</conclusion>':
            ok=0
    i=i+1





file.close()
file2.close()
