# Image Classification using Support Vector Machine (SVM)

This project is a part of the Prodigy Infotech Machine Learning Internship, focusing on implementing a Support Vector Machine (SVM) for image classification.

## Author

- **Author:** Muhammad Awais Akhter
- **GitHub:** [awais-akhter](https://github.com/awais-akhter)

## Problem Statement

The task involves implementing a support vector machine (SVM) to classify images of cats and dogs using the Kaggle dataset.

## Dataset

The dataset contains images of cats and dogs and can be accessed via the following Kaggle link:
[Dataset Link](https://www.kaggle.com/c/dogs-vs-cats/data)

## Implementation Details

### Libraries Used
- `numpy`, `pandas`: Data manipulation and handling
- `zipfile`, `os`: File handling and extraction
- `PIL`, `matplotlib`: Image processing and visualization
- `sklearn`: Machine learning utilities

### Workflow

- **Data Loading and Preprocessing**: Extracted the dataset and prepared the data for training.
- **Visualizing Data**: Displayed random images from the dataset to visualize the contents.
- **Feature Extraction**: Utilized Histogram of Oriented Gradients (HOG) for feature extraction.
- **Model Training**: Employed Support Vector Classifier (SVC) and LinearSVC for training the image classification model.
- **Model Evaluation**: Calculated the accuracy of both SVC and LinearSVC models.

### Conclusion

The implemented models achieved an accuracy of approximately 0.68 in classifying images of cats and dogs.

## Execution

To execute this code locally, follow these steps:
1. Download the dataset from [Kaggle](https://www.kaggle.com/c/dogs-vs-cats/data).
2. Set up the Jupyter Notebook environment or Python with necessary libraries.
3. Execute the code cells in the provided `image-classification-dog-and-cat.ipynb` file.

## Acknowledgments

- Kaggle for hosting the dataset used in this project.

Feel free to explore the code and dataset further for insights and improvements!
