# -*- coding: utf-8 -*-
"""Day_9_DHRUVDHAYAL_AI_ML.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1LH7a-QFZzgtKiDJ4bpBERaOdFycQWH2R

#Neural Networks!
"""

# Step-1: Now, we have to import the Libraries Inbuilt or Pre-defined.
from tensorflow import keras;
import numpy as np;
import matplotlib.pyplot as plt;

#Load the MNIST Datasets from the keras Library.
(Xtrain,ytrain),(Xtest,ytest)=keras.datasets.mnist.load_data();
print(Xtrain.shape,ytrain.shape);
print(Xtest.shape,ytest.shape);

#Data Scaling.
Xtrain=Xtrain/Xtrain.max();
Xtest=Xtest/Xtest.max();

print("\n --> Number of the Labels: ",len(np.unique(ytrain)));

#Visualise the Values of the Data/Informations.
import numpy as np;
plt.figure(1,figsize=(6,8));
for i in range(1,36+1,1):
  temp=np.random.randint(0,60000);
  im=Xtrain[temp,:,:];
  lab=ytrain[temp];
  plt.subplot(6,6,i);
  plt.imshow(im,cmap='gray');
  plt.title(lab);
  plt.axis('off')

#Creating the Neural Networks.
nn_model=keras.Sequential(); #Create the empty 'nn' feed forward.
#Framework.
nn_model.add(keras.layers.Flatten(input_shape=(Xtrain.shape[1],Xtrain.shape[2])));  #An , Input Layer.

#Hidden Layers.
nn_model.add(keras.layers.Dense(128,activation='relu')); # Hidden Layer - 1.
nn_model.add(keras.layers.Dense(256,activation='relu')); # Hidden Layer - 2.
nn_model.add(keras.layers.Dense(256,activation='relu')); # Hidden Layer - 3.

#Output Layer.
nn_model.add(keras.layers.Dense(len(np.unique(ytrain))));

print(nn_model.summary());

#Optimizer Adding.
nn_model.compile(optimizer='SGD',loss=keras.losses.SparseCategoricalCrossentropy(from_logits=True),metrics=['accuracy']) # Changed 'Loss' to 'loss'

#TRrain the model for the Xtrain and Ytrain.
history=nn_model.fit(Xtrain,ytrain,epochs=20);

print(Xtrain.min," - ",Xtrain.max());

# visualize the training loss and acc
plt.figure(1,figsize=(4,2));
plt.plot(history.epoch,history.history['loss'],'--ko');
plt.grid('on');
plt.title('Training loss graph ');
plt.xlabel('Epochs');
plt.ylabel('Loss');

plt.figure(2,figsize=(4,2));
plt.plot(history.epoch,history.history['accuracy'],'--ko');
plt.grid('on');
plt.title('Training accuracy graph ');
plt.xlabel('Epochs');
plt.ylabel('Accuracy');

#Now, Evaluate the Test Data.
[loss,acc]=nn_model.evaluate(Xtest,ytest);
print("\n 1. Loss Values: ",loss);
print("\n 2. Test Accuracy: ",acc);

"""#Importing the Fashion Datsets."""

# Step-1: Now, we have to import the Libraries Inbuilt or Pre-defined.
from tensorflow import keras;
import numpy as np;
import matplotlib.pyplot as plt;

#Load the MNIST Datasets from the keras Library.
(Xtrain,ytrain),(Xtest,ytest)=keras.datasets.fashion_mnist.load_data();
print(Xtrain.shape,ytrain.shape);
print(Xtest.shape,ytest.shape);

#Data Scaling.
Xtrain=Xtrain/Xtrain.max();
Xtest=Xtest/Xtest.max();

print("\n --> Number of the Labels: ",len(np.unique(ytrain)));

#Visualise the Values of the Data/Informations.
import numpy as np;
plt.figure(1,figsize=(6,8));
for i in range(1,36+1,1):
  temp=np.random.randint(0,60000);
  im=Xtrain[temp,:,:];
  lab=ytrain[temp];
  plt.subplot(6,6,i);
  plt.imshow(im,cmap='gray');
  plt.title(lab);
  plt.axis('off')

#Creating the Neural Networks.
nn_model=keras.Sequential(); #Create the empty 'nn' feed forward.
#Framework.
nn_model.add(keras.layers.Flatten(input_shape=(Xtrain.shape[1],Xtrain.shape[2])));  #An , Input Layer.

#Hidden Layers.
nn_model.add(keras.layers.Dense(128,activation='relu')); # Hidden Layer - 1.
nn_model.add(keras.layers.Dense(256,activation='relu')); # Hidden Layer - 2.
nn_model.add(keras.layers.Dense(256,activation='relu')); # Hidden Layer - 3.

#Output Layer.
nn_model.add(keras.layers.Dense(len(np.unique(ytrain))));

print(nn_model.summary());

#Optimizer Adding.
nn_model.compile(optimizer='SGD',loss=keras.losses.SparseCategoricalCrossentropy(from_logits=True),metrics=['accuracy']) # Changed 'Loss' to 'loss'

#TRrain the model for the Xtrain and Ytrain.
history=nn_model.fit(Xtrain,ytrain,epochs=20);

# visualize the training loss and acc
plt.figure(1,figsize=(4,2));
plt.plot(history.epoch,history.history['loss'],'--ko');
plt.grid('on');
plt.title('Training loss graph ');
plt.xlabel('Epochs');
plt.ylabel('Loss');

plt.figure(2,figsize=(4,2));
plt.plot(history.epoch,history.history['accuracy'],'--ko');
plt.grid('on');
plt.title('Training accuracy graph ');
plt.xlabel('Epochs');
plt.ylabel('Accuracy');

#Now, Evaluate the Test Data.
[loss,acc]=nn_model.evaluate(Xtest,ytest);
print("\n 1. Loss Values: ",loss);
print("\n 2. Test Accuracy: ",acc);

"""#CIFAR DATSETS."""

# Step-1: Now, we have to import the Libraries Inbuilt or Pre-defined.
from tensorflow import keras;
import numpy as np;
import matplotlib.pyplot as plt;

#Load the MNIST Datasets from the keras Library.
(Xtrain,ytrain),(Xtest,ytest)=keras.datasets.cifar10.load_data();
print(Xtrain.shape,ytrain.shape);
print(Xtest.shape,ytest.shape);

#Data Scaling.
Xtrain=Xtrain/Xtrain.max();
Xtest=Xtest/Xtest.max();

print("\n --> Number of the Labels: ",len(np.unique(ytrain)));

#Visualise the Values of the Data/Informations.
import numpy as np;
plt.figure(1,figsize=(6,8));
for i in range(1,36+1,1):
  temp=np.random.randint(0,50000); # Generate random integers within the valid range
  im=Xtrain[temp,:,:];
  lab=ytrain[temp];
  plt.subplot(6,6,i);
  plt.imshow(im,cmap='gray');
  plt.title(lab);
  plt.axis('off')

#Creating the Neural Networks.
nn_model=keras.Sequential(); #Create the empty 'nn' feed forward.
#Framework.
nn_model.add(keras.layers.Flatten(input_shape=(Xtrain.shape[1],Xtrain.shape[2], Xtrain.shape[3])));  #An , Input Layer. # Added Xtrain.shape[3] to account for color channels

#Hidden Layers.
nn_model.add(keras.layers.Dense(128,activation='relu')); # Hidden Layer - 1.
nn_model.add(keras.layers.Dense(256,activation='relu')); # Hidden Layer - 2.
nn_model.add(keras.layers.Dense(256,activation='relu')); # Hidden Layer - 3.

#Output Layer.
nn_model.add(keras.layers.Dense(len(np.unique(ytrain)))); # Removed the dense layer that was causing the shape mismatch

print(nn_model.summary());

#Optimizer Adding.
nn_model.compile(optimizer='SGD',loss=keras.losses.SparseCategoricalCrossentropy(from_logits=True),metrics=['accuracy']) # Changed 'Loss' to 'loss'

#TRrain the model for the Xtrain and Ytrain.
history=nn_model.fit(Xtrain,ytrain,epochs=50);

# visualize the training loss and acc
plt.figure(1,figsize=(4,2));
plt.plot(history.epoch,history.history['loss'],'--ko');
plt.grid('on');
plt.title('Training loss graph ');
plt.xlabel('Epochs');
plt.ylabel('Loss');

plt.figure(2,figsize=(4,2));
plt.plot(history.epoch,history.history['accuracy'],'--ko');
plt.grid('on');
plt.title('Training accuracy graph ');
plt.xlabel('Epochs');
plt.ylabel('Accuracy');

#Now, Evaluate the Test Data.
[loss,acc]=nn_model.evaluate(Xtest,ytest);
print("\n 1. Loss Values: ",loss);
+print("\n 2. Test Accuracy: ",acc);

