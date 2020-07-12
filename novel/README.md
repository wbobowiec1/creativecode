# Generate A Novel Of My Own

This project folder contains an example for generating a novel, as definied by [NaNoGenMo](http://nanogenmo.github.io). 


## Tracery Bookery
The enclosed [story.json](story.json) file is a Tracery grammar that should expand a few sentences into something like 50,000 words. The actual word count will vary based on the length and number of the core sentences.

This JSON file can be dropped into [this template](https://github.com/zachwhalen/bookery).

Here is the cleaner look of the program [Copy_of_TextGenerationPyTracery.ipynb](https://github.com/wbobowiec1/CreativeCodeClass/blob/master/Copy_of_TextGenerationPyTracery.ipynb)

I used [Colab Notebook](https://colab.research.google.com/notebooks/intro.ipynb#recent=true) to create this program. I needed PyTracery to create my program but Colab does not have that on it's own so I had to first install PyTracery to Colab Notebook. Next I needed to install the markdown option and random choice option like I used in my previous project, the poem project [Poem Project](https://github.com/wbobowiec1/creativecode/tree/master/poem). 

Next, I had to set the rules for Tracery that I wanted it to follow so it can properly create a novel and have it say what I want it to say. I wanted to greet my readers before they started reading my novel so I wrpte a code for that first. Then I moved on writing the code so the program would display the title of my book which was the actual title of a book I wrote back in elementary school. Here is the actual story [My Book](https://creationofhands.standupchild.com/uncategorized/the-tales-of-a-seeing-eye-dog-the-adventures-of-fred-the-seeing-eye-dog-by-me/), it is short story more like ocmpared to a novel but I thought this book would be a good choice to use as a template to create my program that will create a novel based on this story I wrote from a long time ago. 

The rest of the code from then on is just writing enough code for the program to generate enough text to be considered at least a novel which is 50k words or more. 

My titles for my chapters are not anything fancy or unique because I wanted to make this novel the program generates to be as close to the short story I had created. My goal was accuracy over anything. No specific reason for having 15 chapters besides to have enough chapters to be considered a good length npvel. 

The sentences were couple of lines that are from each chapter of my short story. I chose those sentences specifically because I wanted the generated novel to create a story that had the important story points in it from my short story I created. 

The last 9 lines of code starting at "novel = grammar.flatten("#origin#")" and ending at "html.write_pdf('/content/novel.pdf',stylesheets=[css],font_config=font_config)", is just code that is saving the novel first as html by using the markdown option then configuring the font I desire and then finally turning the html novel into a pdf novel. 

If you were to make this program yourself you would just need to edit the "orgin" however you like it and if you want different attributes within the origin code than what I already have in there then just change the attribute lists up. Or you can always not have a greeting in the beginning if that is also what you desire. You would do this by deleting the origin code and it's attributes lists it uses and also the print statement that prints the output of that code. Next you could change the book name since my book name in the code is based off of my short story I created and it was what I desired this novel to be called to. Another concept you can change up is the chapter tites. Like I mentioned before I chose the titles I did for accuracy towards my short story I created but you can make those chapters however you like. You can also choose how many chapter titles you want by adding or deleting the code to create more or less chapters. Then you could also edit the sentence code to have as many or as less of sentences you want but also edit it to have whatever sentences you want the program to use as a base line for your novel that will be generated. The paragraphs code section can also be editted to have as many or less sentences within in each paragraph. In chapters code section you would do a similar concept but this time with as many or less paragraphs that you desire to have in each chapter. The last final change you could make is in the font choice or how the novel will be shown in the pdf version of itself. I chose simple rules but if desired you could make it more complex if desired so. 

To make sure my generated novel was at least 50k words or more I used the code "len(novel.split(" "))", that is the code to print out the length of the novel and mine was definitely over 50k. 
