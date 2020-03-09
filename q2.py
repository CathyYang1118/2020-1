def TopLevel():
    while True:
        Info = GetInfo()
        if 65 <= ord(Info[0]) <= 77:
            File = 'File1.txt'
        else:
            File = 'File2.txt' 

        test = WriteInfo(File,Info)

        if not test:
            print('error')
            break

        end = input('input Y/N')

        if end == 'N':
            break
