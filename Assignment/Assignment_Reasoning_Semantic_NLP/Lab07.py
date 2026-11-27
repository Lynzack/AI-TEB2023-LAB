# semantic_network = [
#     ("Airline", "operates", "Flight"),
#     ("Passenger", "books", "Flight"),
#     ("Flight", "has", "Destination"),
#     ("Flight", "has", "Departure Time"),
#     ("Flight", "can", "Delayed"),
#     ("Flight", "can", "Cancelled"),
#     ("Delay" , "cause", "Passenger Complaint")
    
# ]

# for relationship in semantic_network:
#     print(relationship)
# def classify_message(tweet):
#     tweet = tweet.lower()

#     if "cancelled" in tweet or "delayed" in tweet:
#         return "Service Complaint"

#     elif "what time" in tweet or "departure" in tweet:
#         return "Information Request"

#     else:
#         return "Other"

# tweet_a = "My flight has been cancelled"
# tweet_b = "What time does flight AB123 depart?"

# print(classify_message(tweet_a))
# print(classify_message(tweet_b))

import re

def preprocess_text(text):

    # Replace usernames with USER
    text = re.sub(r"@\w+", "USER", text)

    # Replace URLs with URL
    text = re.sub(r"https?://\S+", "URL", text)

    # Convert text to lowercase
    text = text.lower()

    # Remove extra whitespace
    text = re.sub(r"\s+", " ", text).strip()

    return text


tweet = "@SkyAir My flight is NOT good! It was delayed again. https://airline.example"

clean_tweet = preprocess_text(tweet)

print(clean_tweet)

