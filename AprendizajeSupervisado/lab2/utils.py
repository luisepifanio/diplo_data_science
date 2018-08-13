from sklearn.datasets import load_files
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split

import matplotlib.pyplot as plt

import numpy as np
import pandas as pd
import seaborn as sns

import os


def load_datasets_unlabeled_test():
    dataset = load_files(
        'review_polarity_competition/reviews_sentoken', shuffle=False)
    docs_train, docs_dev, y_train, y_dev = train_test_split(
        dataset.data, dataset.target, test_size=0.10, random_state=42)
    dirname = "review_polarity_competition/test_reviews_sentoken"
    test = []
    # I do this to keep the files in numeric order
    for fname in range(len(os.listdir(dirname))):
        fname = str(fname) + ".txt"
        with open(os.path.join(dirname, fname)) as fd:
            test.append(fd.read())
    train = docs_train, y_train
    dev = docs_dev, y_dev
    return train, dev, test


def save_results(fname, labels):
    with open(fname, 'w') as f:
        f.write("Id,Category\n")
        for i, l in enumerate(labels):
            f.write(str(i) + ".txt," + str(l) + "\n")


def print_confusion_matrix(confusion_matrix, class_names, figsize=(10, 7), fontsize=14):
    """Prints a confusion matrix, as returned by sklearn.metrics.confusion_matrix, as a heatmap.

    Arguments
    ---------
    confusion_matrix: numpy.ndarray
        The numpy.ndarray object returned from a call to sklearn.metrics.confusion_matrix. 
        Similarly constructed ndarrays can also be used.
    class_names: list
        An ordered list of class names, in the order they index the given confusion matrix.
    figsize: tuple
        A 2-long tuple, the first value determining the horizontal size of the ouputted figure,
        the second determining the vertical size. Defaults to (10,7).
    fontsize: int
        Font size for axes labels. Defaults to 14.

    Returns
    -------
    matplotlib.figure.Figure
        The resulting confusion matrix figure

    FROM: https://gist.github.com/shaypal5/94c53d765083101efc0240d776a23823
    """
    df_cm = pd.DataFrame(
        confusion_matrix, index=class_names, columns=class_names,
    )
    fig = plt.figure(figsize=figsize)
    try:
        heatmap = sns.heatmap(df_cm, annot=True, fmt="d")
    except ValueError:
        raise ValueError("Confusion matrix values must be integers.")
    heatmap.yaxis.set_ticklabels(
        heatmap.yaxis.get_ticklabels(), rotation=0, ha='right', fontsize=fontsize)
    heatmap.xaxis.set_ticklabels(
        heatmap.xaxis.get_ticklabels(), rotation=45, ha='right', fontsize=fontsize)
    plt.title('Confusion Matrix')
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    return fig


def plot_confusion_matrix(pred, y_val, LABELS):
    # Plot confusion matrix
    cnf_matrix = confusion_matrix(pred, y_val)
    _ = print_confusion_matrix(cnf_matrix, LABELS)

    # Print Precision Recall F1-Score Report
    report = classification_report(pred, y_val, target_names=LABELS)
    print(report)


def train_test_and_evaluate(pipeline, x_train, y_train, x_test, y_test, labels=[0, 1]):

    neg_sentences = x_test[y_test == 0]
    fneg_leng     = ( len(x_test) * 1.0 )  

    if len( neg_sentences ) / fneg_leng > 0.5:
        null_accuracy = len( neg_sentences ) / fneg_leng
    else:
        null_accuracy = 1.0 - ( len( neg_sentences ) / fneg_leng )
    sentiment_fit = pipeline.fit(x_train, y_train)
    y_pred = sentiment_fit.predict(x_test)
    accuracy = accuracy_score(y_test, y_pred)
    conmat = np.array(confusion_matrix(y_test, y_pred, labels))
    confusion = pd.DataFrame(conmat, index=['negative', 'positive'],
                             columns=['predicted_negative', 'predicted_positive'])
    print("null accuracy: {0:.2f}%".format(null_accuracy*100))
    print("accuracy score: {0:.2f}%".format(accuracy*100))
    if accuracy > null_accuracy:
        print("model is {0:.2f}% more accurate than null accuracy".format(
            (accuracy-null_accuracy)*100))
    elif accuracy == null_accuracy:
        print("model has the same accuracy with the null accuracy")
    else:
        print("model is {0:.2f}% less accurate than null accuracy".format(
            (null_accuracy-accuracy)*100))
    print("-"*80)
    print("Confusion Matrix\n")
    print(confusion)
    print("-"*80)
    print("Classification Report\n")
    print(classification_report(y_test, y_pred, target_names=['negative', 'positive']))

    print_confusion_matrix(conmat, labels )
