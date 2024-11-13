
'''

1. Product Review Analysis

'''



#Task 1: Keyword Highlighter


def review_search(reviews):
        for review in reviews:
                review_list = review.split()
                review_string = ' '.join(review_list)
                final_string = review_string.replace("good", "GOOD")
                final_string = final_string.replace("Good", "GOOD")
                final_string = final_string.replace("excellent", "EXCELLENT")
                final_string = final_string.replace("Excellent", "EXCELLENT")
                final_string = final_string.replace("bad", "BAD")
                final_string = final_string.replace("Bad", "BAD")
                final_string = final_string.replace("poor", "POOR")
                final_string = final_string.replace("Poor", "POOR")
                final_string = final_string.replace("average", "AVERAGE")
                final_string = final_string.replace("Average", "POOR")
                
                print(final_string)
        return ''

        
#Task 2
def word_count(words, reviews):
        
        for word in words:
            count = 0
            for i in range(len(reviews)):
                if word in reviews[i].lower():
                    count = word.count(word)
            statement = print(f"{word} count: {count}")
        
        return statement
        

#Task 3

def review_summary(reviews):
    summary = ''
    for review in reviews:
        end = 31
        summary += review[:end] + "...\n"
        
            
    return summary

        
            
                    
                

               

reviews = [
        "This product is really good. I'm impressed with its quality.",
        "The performance of this product is excellent. Highly recommended!",
        "I had a bad experience with this product. It didn't meet my expectations.",
        "Poor quality product. Wouldn't recommend it to anyone.",
        "The product was average. Nothing extraordinary about it."
    ]

positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]


#print Task 1
review_search(reviews)
#print Task 2
word_count(positive_words, reviews)
word_count(negative_words, reviews)
#print Task 3
print(review_summary(reviews))