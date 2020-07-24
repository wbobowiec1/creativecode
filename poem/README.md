# Wenzi's Poem

This project is a poem generator in Python. To see it run, download the [Pride&Prejud.py](https://github.com/wbobowiec1/creativecode/blob/master/poem/Wenzi'spoem.py) and run it with Python or in a notebook. It will require [TextBlob](https://textblob.readthedocs.io), so make sure you've installed that first. 

The file I chose was from [Project Gutenberg](http://www.gutenberg.org/). The file from there was a plain text file of the Pride and Prejudice Book. I chose this book because I wanted a romantic book to go along my love template poem. You can download that here [Pride & Prejudice Book Plain Text](http://www.gutenberg.org/files/1342/1342-0.txt). I wanted to my version of this file to not contain anything but the book so in Notepad that should be on most computers, I pasted the whole plain text file into Notepad after I copied it from it's original source. 
This script also assumes you have a file called "Pride&Prejud.txt" in the same directory that the script runs from. The contents of that file can be anything you want to appropriate from. If you have different files, you can just change the filename reference on line 9 of the script.

What this script will do is read the input file, parse it for parts of speech, then output a stanza of something that is similar to or resembles poetry. The poetic quality of that output will vary widely based on the input. It could sound very logical to very ridiculous.

To help myself with turning the file into an output that looks and has the feeling of a poem so I used a template poem to go based off of and then just replace some words within the template poem with some words from the file. The template poem I used was actually a poem I wrote myself, it is a love poem I wrote about half a year ago for my love, here it is: 

Our Yin-Yang Love
 
You are my Yin and I am your Yang.
Complete only with one another.
Our love is no sunshine and rainbows 
But it is like no other. 
 
Two people and two personalities
With differences, though our hearts resides.
Each of us owns a bit of the other 
For we are the same coin, just two sides.
 
Distance separates us but fear not 
We’ll meet soon, for we are like two rivers
Ever flowing til they come together again.
Beauty of our resolve gives me shivers.
 
Like life and death, our time will eventually end 
But til then, honey, say you won’t let go.
Let me be your rain in your desert
And won’t you be my light to my shadow.
 
There’s so much more I could say but...
I’ve realized something.
For us, falling in love wasn’t just a moment 
It’s a forever and always kind of thing 
 


This is my poem I had created back then. I am hobbyist poet so this is one of my creations I've made lately. But you may choose to make your own or find your own template poem if desired. I chose random singular nouns, plural nouns, and adjectives from within my template poem and replaced those words with singular nouns, plural nouns, and adjectives from the Pride & Prejudice book, I let the program choose those random replacement words. By using the poem generator I created I can get a different poem each time I run the program. To do get the replacement words I set the desired kind of words I had the program parse the desired kind of words into their own individual lists and then when running the random choices, the program will search through the specific list that has the desired kind of word and will choose a random word from there to use as the replacement words. 


