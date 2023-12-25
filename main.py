import string
from collections import Counter    # used for Counter to count sentiment in 7C step.
import matplotlib.pyplot as plt  # for step 8, import matplotlib package inside pyplot as plt so i can use plt whenever i need to use this package

# 1. reading text file (which you want to analysis)
text = open("read.txt", encoding="utf-8").read()

# 2. converting text into lowercase
lower_case = text.lower()

# 3. remove special characters/punctuation from the text
# [str.maketrans(x, y, z)- translate() method to replace any "x" characters with a "y" character. Moreover, "z" -describing which characters to remove from the original string]
cleaned_text = lower_case.translate(str.maketrans('', '', string.punctuation))

# 4. Tokenization - splitting text into words and store them into list
split_words = cleaned_text.split()

# 5. Create list of words which are not necessary for sentiment analysis
unnecessary_words = ["also", "i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
                     "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
                     "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
                     "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
                     "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
                     "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
                     "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
                     "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
                     "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
                     "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

# 6. Removing unnecessary words from the tokenized words list (split_words) using loop because our text file is small.
final_words = []
for word in split_words:
    if word not in unnecessary_words:
        final_words.append(word)

# ---------------- 7. Now Start of NLP Algorithm for counting sentiments--------------------
# 7A. check if the word in the final list is also in sentiments.txt
sentiment_list = []    # Create Empty list to add list of sentiments for step 7B.
with open('sentiments.txt', 'r') as file:   # open the 'sentiments.txt' file but only readonly('r') mode
    for line in file:   # Loop through each line and clear it
        clear_line = line.replace('\n', '').replace(',', '').replace("'",'').strip()    # Extract the word and emotion using split
        word, sentiment = clear_line.split(':')

        #  7B. If word is present -> Add the sentiment to sentiment_list
        if word in final_words:
            sentiment_list.append(sentiment)

print(sentiment_list)

# 7C. At last count each sentiment in the sentiment_list for that need need to import Counter from Collections
c = Counter(sentiment_list)
print(c)


# ----------------8. Sentiments in Graph using matplotlib ------------------
figure, axis = plt.subplots()   # created a subplot that stored in this two variables- figure and axis
axis.bar(c.keys(), c.values())  # used variable axis to create bar graph for values vs keys(sentiments)
figure.autofmt_xdate()          # used figure variable to automatically format the x and y axis to fit them properly
plt.savefig('graph.png')        # save the graph as an image
plt.show()
