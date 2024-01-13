import numpy as np
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from keras.optimizers import Adam
from keras.callbacks import EarlyStopping
from keras.utils import to_categorical
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing.image import img_to_array, array_to_img
from sklearn.model_selection import train_test_split

# Load your processed data
train_images = np.load('train_images.npy')
train_labels = np.load('train_labels.npy')
test_images = np.load('test_images.npy')
test_labels = np.load('test_labels.npy')

# Resize images to (224, 224, 3) as expected by VGG16
train_images_resized = np.array([img_to_array(array_to_img(img).resize((224, 224))) for img in train_images])
test_images_resized = np.array([img_to_array(array_to_img(img).resize((224, 224))) for img in test_images])

# Ensure labels are one-hot encoded and have the correct shape
train_labels_one_hot = to_categorical(train_labels, num_classes=2)
test_labels_one_hot = to_categorical(test_labels, num_classes=2)

# Model definition
model = Sequential()
model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(224, 224, 3)))
model.add(MaxPooling2D(2, 2))
model.add(Flatten())
model.add(Dense(64, activation='relu'))
model.add(Dense(2, activation='softmax'))

# Model compilation and training
model.compile(optimizer=Adam(lr=0.001), loss='binary_crossentropy', metrics=['accuracy'])
early_stopping = EarlyStopping(monitor='val_loss', patience=3, restore_best_weights=True)

# Model training with data augmentation
datagen = ImageDataGenerator(
    rotation_range=20,
    width_shift_range=0.2,
    height_shift_range=0.2,
    horizontal_flip=True,
)
datagen.fit(train_images_resized)
generator = datagen.flow(train_images_resized, train_labels_one_hot, batch_size=32)

# Use the length of your training set for the steps_per_epoch parameter
steps_per_epoch = len(train_images) // 32

# Train the model
model.fit(generator, epochs=10, steps_per_epoch=steps_per_epoch, validation_data=(test_images_resized, test_labels_one_hot), callbacks=[early_stopping])

# Evaluate on test data
test_loss, test_acc = model.evaluate(test_images_resized, test_labels_one_hot)
print(f'Test Accuracy: {test_acc}')
