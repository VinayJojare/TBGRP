import os
import cv2
import numpy as np
from keras.utils import to_categorical
from sklearn.model_selection import train_test_split
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from keras.optimizers import Adam
from keras.callbacks import EarlyStopping
from keras.preprocessing.image import img_to_array, array_to_img

# Define your own function to load images and labels
def load_data(data_dir):
    images = []
    labels = []

    for category in os.listdir(data_dir):
        category_path = os.path.join(data_dir, category)
        label = 0 if category == 'dogs' else 1  # Assign 0 for 'dogs' and 1 for 'cats'

        for filename in os.listdir(category_path):
            img_path = os.path.join(category_path, filename)

            # Read and preprocess the image
            img = cv2.imread(img_path)
            img = cv2.resize(img, (128, 128))  # Resize to a consistent size
            img = img / 255.0  # Normalize pixel values to [0, 1]

            images.append(img)
            labels.append(label)

    return np.array(images), np.array(labels)

# Load and preprocess images
def preprocess_images(images, labels, augment=True):
    processed_images = []
    for img in images:
        img = cv2.resize(img, (128, 128))  # Resize to a consistent size
        img = img / 255.0  # Normalize pixel values to [0, 1]
        processed_images.append(img)
    processed_images = np.array(processed_images)
    processed_labels = to_categorical(labels, num_classes=2)

    if augment:
        datagen = ImageDataGenerator(
            rotation_range=20,
            width_shift_range=0.2,
            height_shift_range=0.2,
            horizontal_flip=True,
        )
        datagen.fit(processed_images)
        train_generator = datagen.flow(processed_images, processed_labels, batch_size=32)

        # Model definition
        model = Sequential()
        model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(128, 128, 3)))  # Adjust input shape
        model.add(MaxPooling2D(2, 2))
        model.add(Flatten())
        model.add(Dense(64, activation='relu'))
        model.add(Dense(2, activation='softmax'))

        # Model compilation and training
        model.compile(optimizer=Adam(lr=0.001), loss='binary_crossentropy', metrics=['accuracy'])
        early_stopping = EarlyStopping(monitor='val_loss', patience=3, restore_best_weights=True)

        # Train the model
        model.fit(train_generator, epochs=10, validation_data=(processed_images, processed_labels), callbacks=[early_stopping])

        # Evaluate on test data
        test_loss, test_acc = model.evaluate(processed_images, processed_labels)
        print(f'Test Accuracy: {test_acc}')

    return np.array(processed_images), to_categorical(labels, num_classes=2)

if __name__ == "__main__":
    data_dir = r"G:\Internships\TrustingBrains\cat vs dog\dataset"  # Use 'r' before the string to handle backslashes in Windows paths
    
    images, labels = load_data(data_dir)
    train_images, test_images, train_labels, test_labels = train_test_split(images, labels, test_size=0.2, random_state=42)
    train_images, train_labels = preprocess_images(train_images, train_labels)
    test_images, test_labels = preprocess_images(test_images, test_labels)

    # ... (rest of the code remains the same)
