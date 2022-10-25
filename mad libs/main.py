import json
import os
from re import template

# mad libs template

class MadLibs:
    path = "/Users/annatopping/Documents/py projects/mad libs/templates"
    def __init__(self, word_descriptions, template):
        self.template = template
        self.word_descriptions = word_descriptions
        self.user_input = []
        self.story = None

    @classmethod
    def from_json(cls, name, path=None):
        if not path:
            path = cls.path
        fpath = os.path.join(path, name)
        #print(os.path.exists(fpath))
        with open(fpath, "r") as f:
            data = json.load(f)
        mad_lib = cls(**data)
        return mad_lib
        #print(mad_lib.word_descriptions)

    def get_words_from_user(self):
        # word_descriptions = ["noun", "verb"]
        print("Please provide the following words: ")
        for desc in self.word_descriptions:
            ui = input(desc + " ") 
            self.user_input.append(ui)
        return self.user_input


    def build_story(self):
        self.story = self.template.format(*self.user_input)
        return self.story

def show_story(self):
    print(story)


def select_template():
    print("Select a Mad Lib from the following list:")
    templates = os.listdir(MadLibs.path)
    template = input(str(templates) + " ")
    return template

temp_name = select_template()

#temp_name = "zoo-story.json"
mad_lib = MadLibs.from_json(temp_name)
words = mad_lib.get_words_from_user()
story = mad_lib.build_story()
mad_lib.show_story()

print(story)
