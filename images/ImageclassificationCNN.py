from keras.models import Sequential
model = Sequential()
model.get_config()
from keras.layers import Convolution2D
model.add(Convolution2D(
        filters = 32,
        kernel_size= (3,3),
        input_shape = (64,64,3)
    ))
from keras.layers import MaxPooling2D
model.add(MaxPooling2D(
                pool_size=(2,2)
))
from keras.layers import Flatten
model.add(Flatten())
model.get_config()
from keras.layers import Dense
model.add(
        Dense(units=128 , activation='relu')
)
model.add(
        Dense(units=64 , activation='relu')
)
model.add(
        Dense(units=32 , activation='relu')
)
model.add(
        Dense(units=1 , activation='sigmoid')
)
from keras_preprocessing.image import ImageDataGenerator
train_datagen = ImageDataGenerator(
        rescale=1./255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)
test_datagen = ImageDataGenerator(rescale=1./255)

train_generator = train_datagen.flow_from_directory(
        'cnn_dataset/training_set/',
        target_size=(64, 64),
        batch_size=32,
        class_mode='binary')
validation_generator = test_datagen.flow_from_directory(
        'cnn_dataset/test_set/',
        target_size=(64, 64),
        batch_size=32,
        class_mode='binary')
model.compile(optimizer='adam' , loss='binary_crossentropy' , metrics=['accuracy'])
model.fit(
        train_generator,
        epochs=10,
        validation_data=validation_generator,)
model.save("mycnnmodel1731Jan.h3")
from keras.models import load_model
m = load_model('mycnnmodel1731Jan.h3')
from keras.preprocessing import image
testimg = image.load_img('img/cat_or_dog_1.jpg' , target_size=(64,64))
type(testimg)
