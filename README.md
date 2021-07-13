# Achilles

Achilles is the name of the project grouping numerous software using different n-grams to guess the language of the input givent by the user.
It uses bigrams or quatergrams most of the time to build a probability distribution model. The model presents the probability of getting certain combinations of characters depending on the language.
The dataset of books is freely provided by https://www.gutenberg.org/. 
The learning algorithm generate first the probability of getting an n-gram depending on the language and store it in a file. When ask about the language of a text, the algorithm will compare the input with the set of n-grams in the file and choose the language with the highest probability.
The more dataset you give to the algorithm the better it will get. With 20 books per language we can achieve up to 94% with quatergrams which is very good.
