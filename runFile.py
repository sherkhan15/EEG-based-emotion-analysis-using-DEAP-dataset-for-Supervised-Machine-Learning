from ConvertData import convertData
from FeaturesSampled import sampleFeatures
from LabelClass0 import onehotencoding0
from LabelClass1 import onehotencoding1
from LabelClass2 import onehotencoding2
from LabelClass3 import onehotencoding3
from cross_validation0 import cross_validate0
from cross_validation1 import cross_validate1
from cross_validation2 import cross_validate2
from cross_validation3 import cross_validate3
from data_visual import data_visual
from svmClassifier import svm_classifier
from svmClassifierLDA import svm_classifier_lda
from svmClassifierLDARSCV import svm_classifier_lda_rscv
from svmClassifierPCA import svm_classifier_pca
from knnClassifier import knn_classifier
from knnClassifierLDA import knn_classifier_lda
from knnClassifierPCA import knn_classifier_pca
from Russell_circumplex import Russell_circumplex
from display_emotion import Display_emotion

if __name__ == '__main__':
    print('Load Data:\n')
    convertData()
    print('Downsampling features of  Original Data:\n\n')
    sampleFeatures()
    print('Data_visualization')
    data_visual()
    print('Encoding Classes:\n\n')
    onehotencoding0()
    onehotencoding1()
    onehotencoding2()
    onehotencoding3()
    print('Begin Cross Validation:\n')
    print('\nLabel 0\n')
    cross_validate0()
    print('\nLabel 1\n')
    cross_validate1()
    print('\nLabel 2\n')
    cross_validate2()
    print('\nLabel 3\n')
    cross_validate3()
    print('Simple KNN classification: \n\n')
    knn_classifier()
    print('Simple SVM classification: \n\n')
    svm_classifier()
    print('KNN with PCA classification: \n\n')
    knn_classifier_pca()
    print('SVM with PCA classification: \n\n')
    svm_classifier_pca()
    print('KNN with LDA classification: \n\n')
    knn_classifier_lda()
    print('SVM with LDA and RandomizedSearchCV classification: \n\n')
    svm_classifier_lda_rscv()
    print('SVM with LDA classification: \n\n')
    svm_classifier_lda()
    print('Applying Russell circumplex model for emotion \n\n')
    Russell_circumplex()
    print('Displaying Emotion \n\n')
    Display_emotion()
    
    
