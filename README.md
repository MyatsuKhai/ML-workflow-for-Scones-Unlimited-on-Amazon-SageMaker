# ML-workflow-for-Scones-Unlimited-on-Amazon-SageMaker
An image classification model that can automatically detect which kind of vehicle delivery drivers have, in order to route them to the correct loading bay and orders. Assigning delivery professionals who have a bicycle to nearby orders and giving motorcyclists orders that are farther can help Scones Unlimited optimize their operations.

# Introduction
We will be classifying between *Bicycles* and *Motorcycles* images from [CIFER-100 dataset](https://www.cs.toronto.edu/~kriz/cifar.html), using Sagemaker's inhouse image classification algorithm and operationalizing the workflow with statemachine.

# Dataset
Dataset is get from CIFER-100 home page, but we will only use Motorcycles and Bicycle images, so create a data frame, drop all the necesary labels with a function ```unnesdrop()``` and upload the required images to S3 bucket with ```aws sync``` command.
# Training
We use Sagemaker's inhouse image classification algorithm with easy to apply parameters and hyperparameter. You can chek more about this model here. 
[Sagemaker Image Classification Model](https://docs.aws.amazon.com/sagemaker/latest/dg/image-classification.html).
Note that this algorithm asks for a metadadata file, so we need to provide it.
Training is on **ml.p2.xlarge** instance and the training job only takes aroung 1141 seconds with accuracy around 0.8

# Inference Endpoint
After that we use sagemaker's endpoint option to deploy the model as a usable endpoint.
Using Lambda functions to collect and predict the input data and a function to see low confidence attamps, and Combining all together as a statemachine using AWS's step function. 
