# naive_bayes_algorithm

naive bayes algorithm for data mining. The project is my homework.

only run testing() method. testSet.csv is our test data set and trainSet.csv is our train data set.

Used csv lib and math lib. There is no lib for algorithm.

“trainSet.csv” adlı dosyada bulunan eğitim (train) ve “testSet.csv” adlı dosyada bulunan test verileri kullanılarak Naive Bayes algoritması kodlanacak ve ikili sınıflandırma yapılacaktır. 

Veri Seti ile ilgili bilgiler: 
---
- Her değişken, (virgül işareti) ile ayrılmıştır. Bazı değişkenler kayıp değer içermekte olup bu değerler ? ile gösterilmiştir. 
- En sondaki “class” adlı değişken, ikili sınıflandırmaya ilişkin sınıf değişkenidir. “good” etiketi pozitif  (birincil öncelikli), “bad” etiketi negatif (ikincil öncelikli) olanları gösterir. 
- Eğitim setinde 750 adet, test setinde 250 adet kayıt bulunmaktadır.

Program, önce eğitim dosyasını açarak karar ağacını oluşturacak, sonra da oluşan karar ağacı modeline göre, test veri setini kullanarak Accuracy, True Positive Rate, True Negative Rate, True Positive Adedi, True Negative Adedi ölçümlerinin sonucunu ekrana yazdıracaktır.
