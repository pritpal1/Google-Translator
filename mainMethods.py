from googletrans import Translator, LANGUAGES
# print(LANGUAGES)
class MyTranslator:
    def __init__(self):
        #getting all languages and convert it into list
        self.langs = list(LANGUAGES.values())

    def run(self,txt="Type text here",src='english',dest='hindi'):
        #object of Translator()
            self.translator = Translator()
            self.txt = txt
            self.src =  src
            self.dest = dest
            try:
                self.translated = self.translator.translate(self.txt,
                                     src=self.src,dest=self.dest)

            except:
                self.translated = self.translator.translate(self.txt)
            return self.translated.text
            #self.ttext = self.translated.text
            #return self.ttext                                                            