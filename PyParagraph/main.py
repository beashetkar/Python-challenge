# You get to play the role of chief linguist at a local learning academy. As chief linguist, 
# you are responsible for assessing the complexity of various passages of writing, ranging from the sophomoric 
# Twilight novel to the nauseatingly high-minded research article. Having read so many passages, you've since come up with a 
# fairly simple set of metrics for assessing complexity.

# 
# Your task is to create a Python script to automate the analysis of any such passage using these metrics. 
# Your script will need to do the following:
#
# 1) Import a text file filled with a paragraph of your choosing. 
# 2) Assess the passage for each of the following:
# 3) Approximate word count
# 4) Approximate sentence count
# 5) Approximate letter count (per word)
# 6) Average sentence length (in words)

import os
import csv
import re

# Ask for the  text file to read.

input_file = input("Enter the text file with a paragraph: ")

# Give the output text file.txt 

output_file = input("Enter the output file.txt name: ")

# Look for the input text file

input_path = os.path.join("Resources", input_file)

try:

    # Reading the input text file

    with open(input_path, 'r') as filetxt:

        # Should read a complete sentence if line changes so 
        # remove the lines

        paragraph = filetxt.read().replace("\n", " ")

        # Find the sentences in the paragraph removing punctuation (. ? !)
        
        sentences_lst = re.split("(?<=[.!?]) +", paragraph)
        num_sentences = len(sentences_lst)

        #  Create a list to hold all the words in paragraph 
        words_lst = re.split("\W+", paragraph)
        num_words = len(words_lst)

        # Loop through the word list and calculate the lenght of each word

        num_letters = []

        for word in words_lst:
            num_letters.append(len(word))

        # Calculate the letter count (per word) (average)    
        
        avg_len_word = sum(num_letters)/float(len(num_letters))

        # Loop through the sentence list and calculate the number of words in 
        # each sentence

        words_sentence = []

        for sentence in sentences_lst:
            words_sentence.append(len(sentence.split(" ")))

        # Calculate the Average sentence length (in words)

        avg_len_sentence = sum(words_sentence)/float(len(words_sentence))
      
except IOError:

    print ("Path : " + text_path)
    print ("File cannot be opened: " + filename )
    exit()

# Print the results to terminal

print ("Paragraph Analysis")
print ("------------------------------------------------")
print ("Approximate Word Count : " + str(num_words) )
print ("Approximate Sentence Count:  " + str(num_sentences))
print ("Average Letter Count: " + str("{0:.2f}%".format(avg_len_word)))
print ("Average Sentence Length: " + str("{0:.2f}%".format(avg_len_sentence)))

# Save the results to a text file of your choice.

output_path = os.path.join("Output", output_file)

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as output_txt:

   # Write the first row "Header of the File

	output_txt.write("Paragraph Analysis \n")
	output_txt.write("------------------------------------------------\n")

	# Write the results in the next rows
	output_txt.write("Approximate Word Count : " + str(num_words) + "\n")
	output_txt.write("Approximate Sentence Count:  " + str(num_sentences) + "\n")
	output_txt.write("Average Letter Count: " + str("{0:.2f}%".format(avg_len_word)) + "\n")
	output_txt.write("Average Sentence Length: " + str("{0:.2f}%".format(avg_len_sentence)) + "\n")
	

    
        





