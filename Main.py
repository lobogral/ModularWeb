def getModule(file, identation):
    text = ""
    with open(file) as linesText:
        for lineText in linesText:
            text = text + " "*identation + lineText
    return text + "\n"

outputFile = open("holaMundo.html","w") 
outputFile.write("<html>\n")
outputFile.write("  <head>\n")
outputFile.write("    <title>HTML</title>\n")
outputFile.write("  <head>\n")
outputFile.write("  <body>\n")
outputFile.write("    Esto es HTML!\n")
outputFile.write(getModule("modulo1.html", 6))
outputFile.write(getModule("modulo2.html", 6))
outputFile.write("  </body>\n")
outputFile.write("</html>\n")
outputFile.close() 
