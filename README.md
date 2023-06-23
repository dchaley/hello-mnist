# Hello, MNIST

Objective: train, deploy, and get online predictions from a Tensorflow model to recognize handwritten digits.

See also: [MNIST Database](https://en.wikipedia.org/wiki/MNIST_database)

Tasks:

- Train a Tensorflow model on the MNIST dataset

Start from [this Tensorflow MNIST notebook sample](https://colab.research.google.com/github/tensorflow/docs/blob/4d512c2d7c40d69fcb842978aeaa136e19abe2bb/site/en/tutorials/quickstart/beginner.ipynb).

- Deploy model to a Vertex AI endpoint for predictions

Follow [these docs](https://cloud.google.com/vertex-ai/docs/general/deployment).

- Deploy a cloud function to identify uploaded images

Follow [this guide](https://cloud.google.com/blog/products/ai-machine-learning/how-to-serve-deep-learning-models-using-tensorflow-2-0-with-cloud-functions) but use Vertex AI model (vs loading from storage ourselves).
