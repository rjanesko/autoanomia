This script automates the creation of cards for the print and play version of Anomia, by https://www.anomiapress.com/
It takes categories written in categories.txt (up to 15 characters), randomizes the order, and outputs sheets of cards (output.png) with the categories in the proper positions. Cards are only created in sets of 8 - any leftover categories or categories that are too long are output in leftovers.txt

Both the source code and an exe are included.

------------------------------------------------

Enter categories into categories.txt separated by commas.
15 max character limit for each category.
If there are fewer than 8 categories in categories.txt, the program will not produce an output.

You can enter categories like:

Example1,Example2,Example3

or

Example1,
Example2,
Example3 

