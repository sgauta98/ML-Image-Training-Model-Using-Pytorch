# ML-Image-Training-Model-Using-Pytorch
Created a pytorch model using the efficientnet b0 model from timm library. This model was used due to its integration with the PyTorch ecosystem. Additionally, it is pre-trained on large datasets which allows for transfer learning in this pytorch image classification model. The b0 model specifically was chosen due to its architecture which scales the depth, width and resolution of the network resulting in a balance between accuracy and efficiency within the model. 
The data was batched prior to being given to the created model and the model was trained through epochs. Training loss, validation loss and F1 scores were all displayed to analyze the accuracy of the model. Cross entropy loss was used since my data was a multi-class classification (4 classes). 

Step-by-step code and analysis is provided in the .ipynb file
