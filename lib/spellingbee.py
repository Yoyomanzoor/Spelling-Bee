from IPython.display import display, Markdown, clear_output
from ipywidgets import *
import webbrowser
import random

def categorize(assignment):
    output = {'1':[],'2':[],'3':[],'4':[],'5':[]}
    for (x,y) in assignment:
        if y in output:
            output[y].append(x)
        else:
            output[y] = [x]
    for x in output:
        output[x] = random.sample(output[x],len(output[x]))
    return(output)

def initialize(wordlist):
    difficulty = [x.split(' ')[0] for x in wordlist.split("\n")]
    words = [x.split(' ')[1].replace(",","") for x in wordlist.split("\n") if x != ['']]
    definitions = dict(zip(words,[' '.join(x.split(' ')[2:]) if x.split(' ')[2] != 'is' and x.split(' ')[2] != 'means' else ' '.join(x.split(' ')[3:]) for x in wordlist.split("\n")]))

    difficulty = categorize(list(zip(words,difficulty)))

    used_words = {'1':[],'2':[],'3':[],'4':[],'5':[]}

    return(difficulty,words,definitions,used_words)

def start_game(words, definitions, difficulty, used_words):

    difficulty_choice = Dropdown(options=['1','2','3','4','5'],description="Difficulty")

    def choose(b):
        try:
            clear_output()
            display(difficulty_choice,word_choice)
            interact_value = difficulty_choice.get_interact_value()
            w = difficulty[interact_value][0]
            used_words[interact_value].append(w)
            difficulty[interact_value] = difficulty[interact_value][1:]
            url = "https://translate.google.com/#view=home&op=translate&sl=en&tl=en&text=" + w
            url2 = "https://www.etymonline.com/search?q=" + w
            m = "Word: " + w + "<br>Definition: " + definitions[w] + "<br>Category: " + interact_value + \
                "<br><sup><a href=\"" + url + "\" target=\"_blank\">google translate</a> " + \
                "| <a href=\"" + url2 + "\" target=\"_blank\">etymology</a></sup>"
            
            display(Markdown(m))
            webbrowser.open_new_tab(url2)
            webbrowser.open_new_tab(url)
        except IndexError:
            m = "No more words left in this category"
            display(Markdown(m))

    word_choice = Button(description="Select a word")
    word_choice.on_click(choose)

    display(difficulty_choice,word_choice)
    return(difficulty,used_words)

def words_in_categories(categories):
    print("Words Left" + 
        "\nTotal: " + str(sum([len(categories[x]) for x in categories])) +
        "\nIn each category:" +
        "\n1: " + str(len(categories['1'])) + 
        "\n2: " + str(len(categories['2'])) + 
        "\n3: " + str(len(categories['3'])) + 
        "\n4: " + str(len(categories['4'])) + 
        "\n5: " + str(len(categories['5'])) +
        "\n\nRun this cell again to refresh")

def words_left(used_words):
    print("Used words " + 
        "\n1: " + ", ".join(used_words['1']) +
        "\n2: " + ", ".join(used_words['2']) +
        "\n3: " + ", ".join(used_words['3']) +
        "\n4: " + ", ".join(used_words['4']) +
        "\n5: " + ", ".join(used_words['5']) +
        "\n\nRun this cell again to refresh")