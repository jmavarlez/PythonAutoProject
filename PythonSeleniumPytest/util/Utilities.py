class Utilities:
    def findstring(fullstring,substring):
        if substring in fullstring:
            return True
        else:
            return False

    def removechar(fullstring,char):
        if isinstance(fullstring, list) == True:
            replacedlist = [string.replace(char,"") for string in fullstring]
            return replacedlist
        else:
            return fullstring.replace(char,"")


    def replacestring(fullstring,findstr,replacestr):
        if isinstance(fullstring, list) == True:
            replacedlist = [string.replace(findstr,replacestr) for string in fullstring]
            return replacedlist
        else:
            return fullstring.replace(findstr,replacestr)
