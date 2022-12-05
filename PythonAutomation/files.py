var = input('Write here anything')
fw = open('doc/file.txt', 'a')
fw.write(var)
fw.close()


# а - запись новых данных в фвйл  и помещение их в конец файла
# w - запись новых данных в фвйл  но с удаление старых

fw = open('doc/file2.txt', 'w')
fw.write('Hello my dear friend')
fw.close()

fr = open('doc/file.txt', 'r')
text = fr.read()
fr.close()

print(text)


