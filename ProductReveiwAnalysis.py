



# Task 1: Keyword Highlighter
# Write a program that searches through a series of product reviews for keywords such as "good", "excellent", "bad", "poor", and "average". 
# Print out each review with the keywords in uppercase so they stand out.

reviews = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "Poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."
]

keywords = ["good", "excellent", "bad", "poor", "average"]

for review in reviews:
    highlightedReview = review
    for keyword in keywords:
        highlightedReview = highlightedReview.replace(keyword, keyword.upper())
    print(highlightedReview)

# Task 2: Sentiment Tally
# Develop a function that tallies the number of positive and negative words in each review. Use a predefined list of positive 
# and negative words to check against. The function should return the count of positive and negative words for each review.

def tally(review):
    positiveWords = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
    negativeWords = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]
   
    positive = sum(review.lower().count(word) for word in positiveWords)
    negative = sum(review.lower().count(word) for word in negativeWords)
   
    return positive, negative

for review in reviews:
    positive, negative = tally(review)
    print(f"Review: {review}")
    print(f"Positive words: {positive}")
    print(f"Negative words: {negative}")

# Task 3: Review Summary
# Implement a script that takes the first 30 characters of a review and appends "…" to create a summary. 
# Ensure that the summary does not cut off in the middle of a word.

def reviewSummary(review):
    summary = review[:30]
    if len(review) > 30:
    
        last_space_index = summary.rfind(' ')
        if last_space_index != -1:
            summary = summary[:last_space_index]
        summary += "…"
    return summary

for review in reviews:
    summary = reviewSummary(review)
    print(f"Review: {review}")
    print(f"Summary: {summary}")

