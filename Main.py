def getModule(file, identation):
    text = ""
    with open(file) as linesText:
        for lineText in linesText:
            text = text + " "*identation + lineText
    return text + "\n"

outputFile = open("holaMundo.html","w") 
outputFile.write(getModule("InitialPage.html", 0))
outputFile.write(getModule("ModulePage1.html", 6))
outputFile.write(getModule("ModulePage2.html", 6))
outputFile.write(getModule("FinalPage.html", 0))
outputFile.close() 
