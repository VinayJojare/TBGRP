# plagiarism_detector_app/views.py
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .forms import TextComparisonForm
from .models import TextComparison
from plagiarism_detector_app.feature_extraction import plagiarized_text, TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def plagiarism_detector(original_text, suspicious_text):
    corpus = [original_text, suspicious_text]
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(corpus)
    similarity_matrix = cosine_similarity(tfidf_matrix)
    similarity_score = similarity_matrix[0, 1]
    return similarity_score
    
def plagiarism_detect(request):
    if request.method == 'POST':
        form = TextComparisonForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            similarity_score = plagiarism_detector(instance.original_text, instance.suspicious_text)
            if similarity_score > 0.8:
                instance.result = "Plagiarism  Detected"
                
            else:
                instance.result = "No plagiarism Detected"
                
            instance.save()
            print(instance.result)
            return render(request, 'Output.html', {'instance': instance.result})
            # print(f"result: {instance.result}")
            # return redirect('result', pk=instance.pk)
        else:
            print(f"Form Errors: {form.errors}")
    else:
        form = TextComparisonForm()
        
    return render(request, 'plagiarism_detect.html', {'form': form})

def result(request, pk):
    instance = get_object_or_404(TextComparison, pk=pk)

    return render(request, 'result.html', {'instance': instance})
