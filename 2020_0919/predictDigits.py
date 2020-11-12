import sklearn.datasets
import sklearn.svm
import PIL.Image
import numpy

#画像ファイルを数値リストに交換する
def imageToData(filename):
    #画像を8x8のグレースケールに交換
    grayImage = PIL.Image.open(filename).convert('L')
    grayImage = grayImage.resize((8,8),PIL.Image.ANTIALIAS)
    #数値リストに変換
    numImage = numpy.asarray(grayImage, dtype = float)
    numImage = numpy.floot(16 - 16 * (numImage / 256))
    numImage = numImage.flatter()

    return numImage

#数字を予測する
def predictDigits(data):
    #学習用データを読み込む
    digits = sklearn.datasets.load_digits()
    #機械学習する
    clf = sklearn.svm.SVC(gamma = 0.001)
    clf.fit(digits.data, digits.target)
    #予測結果を表示する
    n = clf.predict([data])
    print('予測=',n)

#画像ファイルを数値リストに変換する
data = imageToData('2.png')
predictDigits(data)

