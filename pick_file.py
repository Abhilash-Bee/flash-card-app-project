import pandas
from tkinter import messagebox


class PickFile:
    def __init__(self):
        self.lang_dict = {}
        self.pick()

    def pick(self):
        try:
            data = pandas.read_csv("words_to_learn.csv")
        except FileNotFoundError:
            try:
                data = pandas.read_csv("french_words.csv")
            except FileNotFoundError:
                messagebox.showinfo(title="oops", message="File doesn't exists")
            else:
                self.lang_dict = {row.French: row.English for index, row in data.iterrows()}
        else:
            self.lang_dict = {row.French: row.English for index, row in data.iterrows()}

    def create_non_guessed_file(self, data):
        final_data = []
        data.update(self.lang_dict)
        for key, value in data.items():
            to_learn = [
                {
                    "French": key,
                    "English": value,
                }
            ]
            final_data += to_learn

        data = pandas.DataFrame(final_data)
        data.to_csv("words_to_learn.csv", index=False)


