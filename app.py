from pywebio.input import *
from pywebio.output import *
import pywebio
import random
from flask import Flask
app=Flask(__name__)
pywebio.config(css_style="* { background-color:#FFDAE9 }",title="Hangman",theme='sketchy') 
put_text("Hangman game").style('color: #E0B0FF; font-size: 60px')
words=["adeeba","file","carpool","print","chocolate","python","where"]
word = random.choice(words)
def hangman(word):
    l1 = ["." for _ in range(len(word))]
    put_text("Your word is:").style('font-size:40px')
    str1=" ".join(l1)
    
    with use_scope("A"):
        put_text('%s' %str1).style('font-size:60px')
    guess = 5
    while True:
        ch = input("Enter your guess: ",required=True)
        if ch not in word:
            guess -= 1
            with use_scope("B"):
                clear("B")
                put_text("Wrong guess. No of guesses left %s" %guess).style('font-size:40px')
        else:
            cnt = word.count(ch)
            if cnt == 1:
                l1[word.index(ch)] = ch
                clear("A")
                clear("B")
                put_text(" ".join(l1),scope="A").style('font-size:60px')
            else:
                indexes = [i for i in range(len(word)) if word[i]==ch]
                for i in indexes:
                    l1[i] = ch
                clear("A")
                clear("B")
                put_text(" ".join(l1),scope="A").style('font-size:60px')
        if guess == 0:
            clear("B")
            put_text("You lost",scope="B").style('font-size:40px')
            break
        if "." not in l1:
            clear("B")
            put_text("You guessed your word correctly",scope="B").style('font-size:40px')
            break
hangman(word)
if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

