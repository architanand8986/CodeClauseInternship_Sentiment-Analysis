from textblob import TextBlob

def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

def main():
    print("Sentiment Analysis Tool")

    while True:
        user_input = input("\nEnter text (or type 'exit' to quit): ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        sentiment = analyze_sentiment(user_input)
        print(f"Sentiment: {sentiment}")

if __name__ == "__main__":
    main()
