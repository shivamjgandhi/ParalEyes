from keras.applications import VGG16 
from keras.preprocessing.image import ImageDataGenerator
import os
import cv2

#Load the VGG model
image_size1 = 480
image_size2 = 640
vgg_conv = VGG16(weights='imagenet', 
                 include_top=False, 
                 input_shape=(image_size1, image_size2, 3))

# Freeze the layers except the last 4 layers
for layer in vgg_conv.layers[:-4]:
    layer.trainable = False
    
# Check the trainable status of the individual layers
for layer in vgg_conv.layers:
    print(layer, layer.trainable)
    
from keras import models
from keras import layers
from keras import optimizers

# Create the model
model = models.Sequential()

# Add the vgg convolutional base model
model.add(vgg_conv)

# Add new layers
model.add(layers.Flatten())
model.add(layers.Dense(1024, activation='relu'))
model.add(layers.Dropout(0.5))
model.add(layers.Dense(5, activation='softmax'))

# Show a summary of the model. Check the number of trainable params
model.summary()
from keras.preprocessing.image import ImageDataGenerator

#Change the batchsize according to the system RAM
train_batchsize = 100
val_batchsize = 10

train_dir='training_data/train'
validation_dir='training_data/validation'

def generate_data(directory, batch_size):
    """Replaces Keras' native ImageDataGenerator."""
    i = 0
    file_list = os.listdir(directory)
    while True:
        image_batch = []
        for b in range(batch_size):
            if i == len(file_list):
                i = 0
                random.shuffle(file_list)
            sample = file_list[i]
            i += 1
            image = cv2.resize(cv2.imread(sample[0]), (image_size1, image_size2))
            image_batch.append((image.astype(float) - 128) / 128)

        yield np.array(image_batch)

train_batch = generate_data(train_dir, train_batchsize)
val_batch = generate_data(validation_dir, val_batchsize)

# Compile the model
model.compile(loss='categorical_crossentropy',
              optimizer=optimizers.RMSprop(lr=1e-4),
              metrics=['acc'])

# Train the model
history = model.fit_generator(
    train_batch,
    steps_per_epoch=int(10),
    epochs=30,
    validation_data=val_batch,
    validation_steps=int(10),
    verbose=1)

# Save the model
model.save('small_last4.h5')

acc = history.history['acc']
val_acc = history.history['val_acc']
loss = history.history['loss']
val_loss = history.history['val_loss']

epochs = range(len(acc))

import matplotlib.pyplot as plt

plt.plot(epochs, acc, 'b', label='Training acc')
plt.plot(epochs, val_acc, 'r', label='Validation acc')
plt.title('Training and validation accuracy')
plt.legend()

plt.figure()

plt.plot(epochs, loss, 'b', label='Training loss')
plt.plot(epochs, val_loss, 'r', label='Validation loss')
plt.title('Training and validation loss')
plt.legend()

plt.show()
