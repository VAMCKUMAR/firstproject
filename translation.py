from translate import Translator
translator = Translator(to_lang="ja")
with open('testfile.txt', mode = 'r') as file1:
	file2 = file1.read()
	translation = translator.translate('file2')
print(translation)
translator= Translator(to_lang="ja")
translation = translator.translate("This is a pen.")
print(translation)

