# Levenshtein Distance
This project builds upon my Document Similarity project, and will be integrated into it shortly after I write this README.md file.

## How I Learned of Levenshtein Distance
The concept of Levenshtein distance was introduced to me when Nate Clark reviewed my Document Similarity project.
I researched what it was and found it quite interesting.
What is Levenshtein distance? 
It's a formula that gives you the minimum amount of change between two words.
These changes can either be Add, Replace, or Delete.

## Converting to Python
Once I understood how to calculate Levenshtein distance by hand, I had to figure out how to make the computer do it. 
After about an hour or two of heavy brainstorming, Nate told me to look up what Dynamic Programming was.
I learned found a video that explained Dynamic Programming as well as memoization, both being a way to only calculate a repeated problem once.
Both concepts seemed very useful, but I decided to use memoization, as that was most similar to doing it by hand.

## Why Two Files?
Main.py is my first successful attempt at recreating Levenshtein Distance.
It works exactly how I want it to, but I wanted to convert it into a callable function.
levenshtein_func.py is just that, a callable function I can import and use in Document Similarity, or in any program I need it.

### Licence
MIT
