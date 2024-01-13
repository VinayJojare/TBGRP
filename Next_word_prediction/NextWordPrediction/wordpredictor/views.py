# wordpredictor/views.py
from django.shortcuts import render, redirect
from .forms import TrainingDataForm, CaptureDataForm
from .utils import train_model, get_combined_data
from .models import CaptureData

def enter_sentence(request):
    form = TrainingDataForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            # Save the entered sentence to the training data
            form.save()

            # Train the model with updated data
            model = train_model()

            # Get the entered sentence from the form
            entered_sentence = form.cleaned_data['sentence']

            # Query for CaptureData instances with the same sentence
            capture_data_instances = CaptureData.objects.filter(sentence=entered_sentence)

            if capture_data_instances.exists():
                # If there are multiple instances, you may want to choose one or handle the situation appropriately
                # For example, you can take the first instance
                predicted_word = capture_data_instances.first().next_word
            else:
                # If not found, use a default value
                predicted_word = 'default_next_word'

            # Pass the predicted word to the template
            return render(request, 'wordpredictor/enter_sentence.html', {'entered_sentence': entered_sentence, 'predicted_word': predicted_word})

    return render(request, 'wordpredictor/enter_sentence.html', {'form': form})


def capture_sentence(request):
    if request.method == 'POST':
        form = CaptureDataForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('wordpredictor:enter_sentence')  # Redirect to enter_sentence view
    else:
        form = CaptureDataForm()

    return render(request, 'wordpredictor/capture_sentence.html', {'form': form})