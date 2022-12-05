import csv
from math import e, pi, sqrt

#train variables
trainHeaders = []
#credit history
creditHistoryValues_good = []
creditHistoryValues_bad = []
#credit amount sample mean
creditAmountSampleMean_good = 0.0
creditAmountSampleMean_bad = 0.0
#credit amount standart deviation
creditAmountStandartDeviation_good = 0.0
creditAmountStandartDeviation_bad = 0.0
#credit amount density func
creditAmountDensityValues_good = []
creditAmountDensityValues_bad = []
#employment
employmentValues_good = []
employmentValues_bad = []
#property magnitude
propertyMagnitudeValues_good = []
propertyMagnitudeValues_bad = []
#age sample mean
ageSampleMean_good = 0.0
ageSampleMean_bad = 0.0
#age standart deviation
ageStandartDeviation_good = 0.0
ageStandartDeviation_bad = 0.0
#age density func
ageDensityValues_good = []
ageDensityValues_bad = []

#train setimizin başlıklarını getirir indisleyerek
def trainerGetHeader():
    with open('trainSet.csv','r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                # names
                for i in row:
                    trainHeaders.append(i)
                break
            break 
        
    return trainHeaders

#ortalama hesaplar age ve creadit amount için bu da density için gerekir
def sampleMeanCalculator(value, classes):
    #credit amount
    if value == "credit_amount":
        with open('trainSet.csv','r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            total_good = 0
            total_bad = 0
            sum_good = 0
            sum_bad = 0

            for row in csv_reader:
                if(row[1] == "?"):
                    line_count +=1    
                else:
                    if row[5] == "good":
                        total_good += 1
                        sum_good = sum_good + int(row[1])
                    elif row[5] == "bad":
                        total_bad += 1
                        sum_bad = sum_bad + int(row[1])

                    line_count+=1

        if classes == "good":
            return sum_good/total_good
        elif classes == "bad":
            return sum_bad/total_bad
    #age
    elif value == "age":
        with open('trainSet.csv','r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            total_good = 0
            total_bad = 0
            sum_good = 0
            sum_bad = 0

            for row in csv_reader:
                if(row[4] == "?"):
                    line_count +=1    
                else:
                    if row[5] == "good":
                        total_good += 1
                        sum_good = sum_good + int(row[4])
                    elif row[5] == "bad":
                        total_bad += 1
                        sum_bad = sum_bad + int(row[4])

                    line_count+=1

        if classes == "good":
            return sum_good/total_good
        elif classes == "bad":
            return sum_bad/total_bad

#credit amount good ve bad için ayrı ortları tutar
creditAmountSampleMean_good = sampleMeanCalculator(value="credit_amount",classes="good")
creditAmountSampleMean_bad = sampleMeanCalculator(value="credit_amount", classes="bad")
#age good ve bad için ayrı ortları tutar
ageSampleMean_good = sampleMeanCalculator(value="age", classes="good")
ageSampleMean_bad = sampleMeanCalculator(value="age",classes="bad")

#standart sapma hesaplar amount credit ve age için density'e lazım
def standartDeviationCalculator(value, classes):
    #credit amount
    if value == "credit_amount":
        aratop_good = 0
        aratop_bad = 0
        aratop2_good = 0
        aratop2_bad = 0
        line_count = 1
        total_good = 0
        total_bad = 0
        sample_good = creditAmountSampleMean_good
        sample_bad = creditAmountSampleMean_bad
        result=0
        with open('trainSet.csv','r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                if(row[1] == "?"):
                    line_count +=1    
                else:

                    if row[5] == "good":
                        aratop2_good = int(row[1])
                        aratop_good = aratop_good + ((aratop2_good - sample_good)**2)
                        total_good += 1
                    elif row[5] == "bad":
                        aratop2_bad = int(row[1])
                        aratop_bad = aratop_bad + ((aratop2_bad - sample_bad)**2)
                        total_bad += 1
                    
                line_count+=1
        
        if classes == "good":
            result = aratop_good/total_good
            return sqrt(result)
        elif classes == "bad":
            result = aratop_bad/total_bad
            return sqrt(result)
    #age
    elif value == "age":
        aratop_good = 0
        aratop_bad = 0
        aratop2_good = 0
        aratop2_bad = 0
        line_count = 1
        total_good = 0
        total_bad = 0
        sample_good = ageSampleMean_good
        sample_bad = ageSampleMean_bad
        result=0
        with open('trainSet.csv','r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                if(row[4] == "?"):
                    line_count +=1    
                else:

                    if row[5] == "good":
                        aratop2_good = int(row[4])
                        aratop_good = aratop_good + ((aratop2_good - sample_good)**2)
                        total_good += 1
                    elif row[5] == "bad":
                        aratop2_bad = int(row[4])
                        aratop_bad = aratop_bad + ((aratop2_bad - sample_bad)**2)
                        total_bad += 1
                    
                line_count+=1
        
        if classes == "good":
            result = aratop_good/total_good
            return sqrt(result)
        elif classes == "bad":
            result = aratop_bad/total_bad
            return sqrt(result)

#credit amount good ve bad için ayrı standart sapmaları tutar
creditAmountStandartDeviation_good = standartDeviationCalculator(value="credit_amount",classes="good")
creditAmountStandartDeviation_bad = standartDeviationCalculator(value="credit_amount", classes="bad")
#age good ve bad için ayrı standart sapmaları tutar
ageStandartDeviation_good = standartDeviationCalculator(value="age", classes="good")
ageStandartDeviation_bad = standartDeviationCalculator(value="age",classes="bad")

#age ve credit amount için density hesaplar x => değerimiz, value => başlık yani feature, classes => sınıfı(good,bad)
def densityFuncValuesFromClass(x,value,classes):
    #credit amount
    if value == "credit_amount":
        ca_sm_good = creditAmountSampleMean_good
        ca_sd_good = creditAmountStandartDeviation_good
        ca_sm_bad = creditAmountSampleMean_bad
        ca_sd_bad = creditAmountStandartDeviation_bad

        if classes == "good":
            result = ((1 / (sqrt(2 * pi) * ca_sd_good)) * e) ** (-1 * (((x - ca_sm_good) ** 2)/(2 * (ca_sd_good ** 2))))
            return float(result)
        elif classes == "bad":
            result = ((1 / (sqrt(2 * pi) * ca_sd_bad)) * e) ** (-1 * (((x - ca_sm_bad) ** 2)/(2 * (ca_sd_bad ** 2))))
            return float(result) 
    #age
    elif value == "age":
        age_sm_good = ageSampleMean_good
        age_sd_good = ageStandartDeviation_good
        age_sm_bad = ageSampleMean_bad
        age_sd_bad = ageStandartDeviation_bad

        if classes == "good":
            result = ((1 / (sqrt(2 * pi) * age_sd_good)) * e) ** (-1 * (((x - age_sm_good) ** 2)/(2 * (age_sd_good ** 2))))
            return float(result)
        elif classes == "bad":
            result = ((1 / (sqrt(2 * pi) * age_sd_bad)) * e) ** (-1 * (((x - age_sm_bad) ** 2)/(2 * (age_sd_bad ** 2))))
            return float(result)

#teste girecek olan trainlerin başlıklara göre dict yapı değişkenleri
testToTrainCreditHistoryGood = {}
testToTrainCreditHistoryBad = {}
testToTrainCreditAmountGood = {}
testToTrainCreditAmountBad = {}
testToTrainEmploymentGood = {}
testToTrainEmploymentBad = {}
testToTrainPropertyMagnitudeGood = {}
testToTrainPropertyMagnitudeBad = {}
testToTrainAgeGood = {}
testToTrainAgeBad = {}

#classlara göre dict yapı değişkenleri
testForGood = {}
testForBad = {}
testClasses = {}
trainClasses = {}

#gelen parametelere göre testToTrain ilgili değişkenlerine atayan fonksiyon x,value,classes her fonksiyonda aynı, 
# rower ise inedxlemek için tutulan bir satır değeri
def trainerGetValuesFromClass(x, value, classes, rower):
    line_count = 1
    #credit history
    if value == "credit_history":
        total_good = 0
        total_bad = 0
        total_leng = 0
        sum_good = 0
        sum_bad = 0
        with open('trainSet.csv','r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                if row[5] == "good":
                    if row[0] == x:
                        sum_good += 1
                    total_good += 1
                elif row[5] == "bad":
                    if row[0] == x:
                        sum_bad += 1
                    total_bad += 1

                total_leng += 1
                line_count += 1
        if classes == "good":
            index = f"credit_history good{x}"
            testToTrainCreditHistoryGood[index] = sum_good / total_good
            
        elif classes == "bad":
            index = f"credit_history bad{x}"
            testToTrainCreditHistoryBad[index] = sum_bad / total_bad
            
    #credit amount
    elif value == "credit_amount":

        if classes == "good":
            res = densityFuncValuesFromClass(x=int(x), value=value, classes=classes)
            index = f"credit_amount good{x}" 
            testToTrainCreditAmountGood[index] = res
            
        elif classes == "bad":
            res = densityFuncValuesFromClass(x=int(x), value=value, classes=classes)
            index = f"credit_amount bad{x}" 
            testToTrainCreditAmountBad[index] = res
            
    #employment
    elif value == "employment":
        total_good = 0
        total_bad = 0
        total_leng = 0
        sum_good = 0
        sum_bad = 0
        with open('trainSet.csv','r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 1
            for row in csv_reader:
                if row[5] == "good":
                    if row[2] == x:
                        sum_good += 1
                    total_good += 1
                elif row[5] == "bad":
                    if row[2] == x:
                        sum_bad += 1
                    total_bad += 1
                
                total_leng += 1
                line_count += 1

        if classes == "good":
            index = f"employment good{x}"
            testToTrainEmploymentGood[index] = sum_good / total_good
            
        elif classes == "bad":
            index = f"employment bad{x}"
            testToTrainEmploymentBad[index] = sum_bad / total_bad
            
    #property magnitude
    elif value == "property_magnitude":
        total_good = 0
        total_bad = 0
        total_leng = 0
        sum_good = 0
        sum_bad = 0
        with open('trainSet.csv','r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 1
            for row in csv_reader:
                if row[5] == "good":
                    if row[3] == x:
                        sum_good += 1
                    total_good += 1
                elif row[5] == "bad":
                    if row[3] == x:
                        sum_bad += 1
                    total_bad += 1

                line_count += 1
        if classes == "good":
            index = f"property_magnitude good{x}"
            testToTrainPropertyMagnitudeGood[index] = sum_good / total_good
            
        elif classes == "bad":
            index = f"property_magnitude bad{x}"
            testToTrainPropertyMagnitudeBad[index] = sum_bad / total_bad
            
    #age
    elif value == "age":

        if classes == "good":
            res = densityFuncValuesFromClass(x=int(x), value=value, classes=classes)
            index = f"age good{x}" 
            testToTrainAgeGood[index] = res
            
        elif classes == "bad":
            res = densityFuncValuesFromClass(x=int(x), value=value, classes=classes)
            index = f"age bad{x}"
            testToTrainAgeBad[index] = res
            

#test fonksiyonu
def testing():
    #değişkenlerimiz
    tp = 0
    tn = 0
    fp = 0
    fn = 0
    accuracy = 0
    tp_rate = 0
    tn_rate = 0
    line_count = 1
    with open('testSet.csv','r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if(row[0] != "?" and row[1] != "?" and row[2] != "?" and row[3] != "?" and row[4] != "?"):
                testClasses[line_count] = row[5]
                i = 0
                for i in range(len(row) - 1):
                    value = trainerGetHeader()[i]
                    classes = row[5]
                    x = row[i]
                    #her satırdaki her özellik için hesaplama yapan fonksiyon çağrıldı
                    trainerGetValuesFromClass(x = x, value = value, classes = classes, rower = line_count)
                
                j = 0
                # for good
                #good değerleri için hesaplar tutan dict
                for j in range(len(row) - 1):
                    value = trainerGetHeader()[j]
                    classes = "good"
                    x = row[j]
                    index = f"{value} {classes}{x}"
                    
                    #credit history
                    chgood = testToTrainCreditHistoryGood.get(index)
                    if chgood != None:
                        chgood = float(chgood)
                    else:
                        chgood = 1
                    #credit amount
                    cagood = testToTrainCreditAmountGood.get(index)
                    if cagood != None:
                        cagood = float(cagood)
                    else:
                        cagood = 1
                    #employment
                    egood = testToTrainEmploymentGood.get(index)
                    if egood != None:
                        egood = float(egood)
                    else:
                        egood = 1
                    #property magnitude
                    pmgood = testToTrainPropertyMagnitudeGood.get(index)
                    if pmgood != None:
                        pmgood = float(pmgood)
                    else:
                        pmgood = 1
                    #age
                    agood = testToTrainAgeGood.get(index)
                    if agood != None:
                        agood = float(agood)
                    else:
                        agood = 1

                    res_good = chgood * cagood * egood * pmgood * agood
                    res_good = float(res_good)

                    testForGood[line_count] = res_good

                k = 0
                # for bad
                #good değerleri için hesaplar tutan dict
                for k in range(len(row) - 1):
                    value = trainerGetHeader()[k]
                    classes = "bad"
                    x = row[k]
                    index = f"{value} {classes}{x}"
                    #credit history
                    chbad = testToTrainCreditHistoryBad.get(index)
                    if chbad != None:
                        chbad = float(chbad)
                    else:
                        chbad = 1
                    #credit amount
                    cabad = testToTrainCreditAmountBad.get(index)
                    if cabad != None:
                        cabad = float(cabad)
                    else:
                        cabad = 1
                    #employment
                    ebad = testToTrainEmploymentBad.get(index)
                    if ebad != None:
                        ebad = float(ebad)
                    else:
                        ebad = 1
                    #property magnitude
                    pmbad = testToTrainPropertyMagnitudeBad.get(index)
                    if pmbad != None:
                        pmbad = float(pmbad)
                    else:
                        pmbad = 1
                    #age
                    abad = testToTrainAgeBad.get(index)
                    if abad != None:
                        abad = float(abad)
                    else:
                        abad = 1

                    res_bad = chbad * cabad * ebad * pmbad * abad
                    res_bad = float(res_bad)

                    testForBad[line_count] = res_bad

                #good classları için ilgili indexteki class bulunur
                y = 0
                for y in range(len(row) - 1):
                    value = trainerGetHeader()[y]
                    classes = "good"
                    x = row[y]
                    index = f"{value} {classes}{x}"

                #bad classları için ilgili indexteki class bulunur
                z = 0
                for z in range(len(row) - 1):
                    value = trainerGetHeader()[z]
                    classes = "bad"
                    x = row[z]
                    index = f"{value} {classes}{x}"
                #tn-tp-fn-fp için karar yapıları
                if float(testForBad.get(line_count)) > float(testForGood.get(line_count)):
                    if testClasses[line_count] == "bad":
                        tn += 1
                    elif testClasses[line_count] == "good":
                        fn += 1

                elif float(testForBad.get(line_count)) < float(testForGood.get(line_count)):
                    if testClasses[line_count] == "bad":
                        fp += 1
                    elif testClasses[line_count] == "good":
                        tp += 1

            line_count += 1
        #oluşan değerlerin yazdırılması
        #accuracy hesaplanması
        accuracy = (tp + tn) / (tp + tn + fp + fn)
        print(f"accuracy: {accuracy}")
        #tp rate hesaplanması
        tp_rate = tp / (tp + fn)
        #tn rate hesaplanması
        tn_rate = tn / (tn + fp)
        print(f"tp rate: {tp_rate}")
        print(f"tn rate: {tn_rate}")
        print(f"fp adedi: {fp}")
        print(f"fn adedi: {fn}")  

# Bu fonksiyonun çalıştırılması gerekmektedir. 
# Diğer fonksiyonların çalıştırılması bu fonksiyonda gereken noktada çağrılarak kodlanmıştır.
testing()