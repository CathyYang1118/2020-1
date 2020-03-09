def GetInf():
    ID=""
    PreferredName=""
    Valid=False
    while Valid == False:
        ID=input("input ID:")
        if len(ID)==5 and ID[0]>="A" and ID[0]<="Z":
            Num = True
            for i in ID[1:]:
                if i not in ['1','2','3','4','5','6','7','8','9','0']:
                    Num = False
            if Num == True:
                Valid = True

    PreferreName=input("input name: ")
    re = ID+"*"+PreferreName
    return re

print(GetInf())
