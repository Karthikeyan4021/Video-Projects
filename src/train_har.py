
# src/train_har.py
# Skeleton HAR model (C3D/I3D idea)
import tensorflow as tf
from tensorflow.keras import layers, models

def build_3dcnn(input_shape=(16,112,112,3), num_classes=10):
    model = models.Sequential([
        layers.Conv3D(32,(3,3,3),activation='relu',input_shape=input_shape),
        layers.MaxPool3D((1,2,2)),
        layers.Conv3D(64,(3,3,3),activation='relu'),
        layers.MaxPool3D((2,2,2)),
        layers.GlobalAveragePooling3D(),
        layers.Dense(num_classes,activation='softmax')
    ])
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    return model

if __name__ == "__main__":
    print("HAR training skeleton. Add dataset loader & clip sampler.")
