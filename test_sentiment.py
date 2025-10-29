from transformers import pipeline

def main():
    print("Loading sentiment analysis model... Please wait")

    # Load multilingual sentiment model
    sentiment_analyzer = pipeline(
        "sentiment-analysis",
        model="cardiffnlp/twitter-xlm-roberta-base-sentiment"
    )

    # Test input
    text = "I feel very happy today!"
    print(f"\nUser input: {text}")

    # Run analysis
    result = sentiment_analyzer(text)[0]

    # Show results
    print(f"\nPredicted sentiment: {result['label']}")
    print(f"Confidence score: {result['score']:.4f}")

if __name__ == "__main__":
    main()
