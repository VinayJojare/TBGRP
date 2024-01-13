# Sample code for TF-IDF vectorization using scikit-learn
from sklearn.feature_extraction.text import TfidfVectorizer
from plagiarism_detector_app.data_processing import original_text


plagiarized_text = "This is some plagiarized text."
corpus = [original_text, plagiarized_text]
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(corpus)

# Example usage:
print(tfidf_matrix.toarray())
