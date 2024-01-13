# wordpredictor/utils.py
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from .models import TrainingData, CaptureData

def get_combined_data():
    training_data = TrainingData.objects.all()
    capture_data = CaptureData.objects.all()

    combined_data = list(training_data) + list(capture_data)
    return combined_data

def train_model():
    data = get_combined_data()

    # Filter out empty sentences
    data = [item for item in data if item.sentence.strip()]

    sentences = [item.sentence for item in data]
    next_words = [getattr(item, 'next_word', 'default_next_word') for item in data]

    print("Data:")
    for item in data:
        print(f"Sentence: {item.sentence}, Next Word: {getattr(item, 'next_word', 'N/A')}")

    if not sentences or not next_words or len(sentences) != len(next_words):
        raise ValueError("Number of non-empty sentences and next words should match.")

    print(f"Number of sentences: {len(sentences)}")
    print(f"Number of next words: {len(next_words)}")

    model = make_pipeline(CountVectorizer(), MultinomialNB())
    model.fit(sentences, next_words)

    return model