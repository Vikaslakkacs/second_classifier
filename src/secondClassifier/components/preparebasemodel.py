
import os
import tensorflow as tf
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.applications import vgg16
from secondClassifier.entity.config_entity import PrepareBasemodelConfig
from pathlib import Path




class PrepareBaseModel:
    def __init__(self, config= PrepareBasemodelConfig):
        self.config= config
    
    def get_base_model(self):
        ##Get VGG16 model
        #print(self.config.include_top)
        self.base_model= vgg16.VGG16(
            include_top=self.config.include_top,
            weights=self.config.weights,
            classes= self.config.classes,
            input_shape= self.config.image_size
        )
        base_model_path= self.config.base_model_path
        self.save_model(model=self.base_model, path=base_model_path)
        #return base_model
    
    def update_base_model(self):
        """Get the base model and create a new model out of it
        """
        ##Get the base model and check to train or un-train
        for layer_num in range (len(self.base_model.layers)):
            self.base_model.layers[layer_num].trainable=False
        ##Create ANN
        flatten= Flatten()(self.base_model.output)
        output_layer= Dense(units=5, activation='softmax')(flatten)

        ##Create new model
        update_model= tf.keras.models.Model(
            inputs= self.base_model.input,
            outputs= output_layer
        )
        ##Compile the model
        update_model.compile(
            loss=tf.keras.losses.CategoricalCrossentropy(),
            optimizer=tf.keras.optimizers.SGD(learning_rate=self.config.learning_rate),
            metrics= ["accuracy"]
        )
        #update_model.summary()
        #update_model.save(self.config.updated_model_path)
        updated_model_path= self.config.updated_model_path
        self.save_model(model=update_model, path=updated_model_path)
       #return update_model
    @staticmethod
    def save_model(model: tf.keras.Model, path: Path):
        #print(save_path)
        model.save(path)
