
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl 


#Ardından bulanık mantık için kullanılacak olan girdi ve çıktı değerleri tanımlanır
#Antecedent ne demek oluyor univers ve label gibi degerlerimiz var label bizim etiketimiz oluyor yani kalite univers te alacağı degerleri koyuyorruz 

#Girdiler
BulaşıkMiktarı=ctrl.Antecedent(np.arange( 0,101,1) , "Bulaşıkmiktar")
KirlilikDerece=ctrl.Antecedent(np.arange(0,101,1) , "KirlilikDerece")
BulaşıkCins=ctrl.Antecedent(np.arange(0,101,1) , "BulaşıkCins")

BulaşıkMiktarı.view()

#***

#Çıktılar
YıkamaZamani=ctrl.Consequent(np.arange(30,161,1) , "YıkamaZamani") 
DeterjanMiktari=ctrl.Consequent(np.arange(0,101,1) , "DeterjanMiktari") 
SuSıcakligi=ctrl.Consequent(np.arange(35,71,1) , "SuSıcakligi") 
UstPompaDevri=ctrl.Consequent(np.arange(2100,3501,1) , "UstPompaDevri") 
AltPompaDevri=ctrl.Consequent(np.arange(2100,3501,1) , "AltPompaDevri") 

#******
#Daha sonra Bulaşıkmiktarı kirlilik derecesi ve bulaşık cınsı için üyelik fonksiyonlarını belirledim otoma
#Daha sonra girdi degerleri olan  Bulaşıkmiktarı kirlilik derecesi ve bulaşık cınsı için üyelik fonksiyonları belirlenir.
#♥Niye 3 çünkü 3 tane durum var iyi kötü orta şeklinde 
#kendisinin yapmasını istedik--->otomatik
BulaşıkMiktarı.automf(3)
KirlilikDerece.automf(3)
BulaşıkCins.automf(3)



#KDerece.view()
#BCins.view()


#***


#Ardından çıktı değeri için üyelik fonksiyonu belirlenir.----->elle
#biz kendimiz belirleyeceği girdiler içinde yapılabilir ama biz orda sistemin kendisini tanımlamasını istedik benzer şekilde çıktı içinde yapabiliriz.



YıkamaZamani["çokKısa"]=fuzz.trimf(YıkamaZamani.universe, [30,30,60]) 
YıkamaZamani["kısa"]=fuzz.trimf(YıkamaZamani.universe, [40,65,90])  
YıkamaZamani["orta"]=fuzz.trimf(YıkamaZamani.universe, [70,95,120])
YıkamaZamani["uzun"]=fuzz.trimf(YıkamaZamani.universe, [100,125,150]) 
YıkamaZamani["çokuzun"]=fuzz.trimf(YıkamaZamani.universe, [130,160,160])  

# YıkamaZamanı.view()

DeterjanMiktari["çokaz"]=fuzz.trimf(DeterjanMiktari.universe, [17.5, 17.5, 17.5]) 
DeterjanMiktari["az"]=fuzz.trimf(DeterjanMiktari.universe, [17.5,30,42.5])  
DeterjanMiktari["normal"]=fuzz.trimf(DeterjanMiktari.universe, [32.5,50,67.5])
DeterjanMiktari["çok"]=fuzz.trimf(DeterjanMiktari.universe, [57.5,75,92.5]) 
DeterjanMiktari["çokfazla"]=fuzz.trimf(DeterjanMiktari.universe, [82.5,100,100])

#DeterjanMiktari.view()



SuSıcakligi["düşük"]=fuzz.trimf(SuSıcakligi.universe, [35,35,50]) 
SuSıcakligi["normal"]=fuzz.trimf(SuSıcakligi.universe, [37.5,52,67.5])  
SuSıcakligi["yüksek"]=fuzz.trimf(SuSıcakligi.universe, [55,70,70])

#SuSıcakligi.view()

UstPompaDevri["çokdüşük"]=fuzz.trimf(UstPompaDevri.universe, [2100,2100,2400]) 
UstPompaDevri["düşük"]=fuzz.trimf(UstPompaDevri.universe, [2300,2500,2700])  
UstPompaDevri["orta"]=fuzz.trimf(UstPompaDevri.universe, [2600,2800,3000])
UstPompaDevri["yüksek"]=fuzz.trimf(UstPompaDevri.universe, [2900,3100,3300]) 
UstPompaDevri["çokyüksek"]=fuzz.trimf(UstPompaDevri.universe, [3200,3500,3500])

#UstPompaDevri.view()

AltPompaDevri["çokdüşük"]=fuzz.trimf(AltPompaDevri.universe, [2100,2100,2400]) 
AltPompaDevri["düşük"]=fuzz.trimf(AltPompaDevri.universe, [2300,2500,2700])  
AltPompaDevri["orta"]=fuzz.trimf(AltPompaDevri.universe, [2600,2800,3000])
AltPompaDevri["yüksek"]=fuzz.trimf(AltPompaDevri.universe, [2900,3100,3300]) 
AltPompaDevri["çokyüksek"]=fuzz.trimf(AltPompaDevri.universe, [3200,3500,3500])

#AltPompaDevri.view()


#**

##kuralları belirleyelim


kural1=ctrl.Rule((BulaşıkMiktarı["poor"] & KirlilikDerece["poor"] & BulaşıkCins["poor"]),( YıkamaZamani["çokKısa"], DeterjanMiktari["çokaz"],  SuSıcakligi["düşük"], UstPompaDevri["çokdüşük"], AltPompaDevri["çokyüksek"]) )





kural2=ctrl.Rule((BulaşıkMiktarı["poor"] & KirlilikDerece["good"] & BulaşıkCins["average"]),( YıkamaZamani["orta"],DeterjanMiktari["normal"],  SuSıcakligi["yüksek"], UstPompaDevri["düşük"], AltPompaDevri["çokyüksek"] ))




kural3=ctrl.Rule((BulaşıkMiktarı["average"] & KirlilikDerece["average"] & BulaşıkCins["good"]),( YıkamaZamani["orta"],  DeterjanMiktari["normal"] ,  SuSıcakligi["normal"], UstPompaDevri["yüksek"], AltPompaDevri["yüksek"]))


kural4=ctrl.Rule((BulaşıkMiktarı["good"] & KirlilikDerece["good"] & BulaşıkCins["average"] ),(YıkamaZamani["çokuzun"],  DeterjanMiktari["çokfazla"],  SuSıcakligi["yüksek"], UstPompaDevri["yüksek"], AltPompaDevri["çokyüksek"]) )




#Kurallardan sonra, makine  sistemini belirleyecek olan kontrol mekanizması tasarlanır.
#diyoruzki kural1 kural2 kural3 vb. kullan bunlara göre bir kontrol mekanizması oluştur...

MakinaKontrol=ctrl.ControlSystem([kural1,kural2,kural3,kural4 ])
#verilecek similasyonu belirliyoruz..
MakinaBelirleme=ctrl.ControlSystemSimulation(MakinaKontrol)

#Ardından girdiler için  değerler verilerek,  ve çıktı  yapılır.
MakinaBelirleme.input["Bulaşıkmiktar"]=22.0
MakinaBelirleme.input["KirlilikDerece"]=92.4
MakinaBelirleme.input["BulaşıkCins"]=80.0

MakinaBelirleme.compute()    #hesaplama fonksiyonunu kullanıyoruz

print(MakinaBelirleme.output["YıkamaZamani"])
print(MakinaBelirleme.output["DeterjanMiktari"])
print(MakinaBelirleme.output["SuSıcakligi"])
print(MakinaBelirleme.output["UstPompaDevri"])
print(MakinaBelirleme.output["AltPompaDevri"])

YıkamaZamani.view(sim=MakinaBelirleme)
DeterjanMiktari.view(sim=MakinaBelirleme)
SuSıcakligi.view(sim=MakinaBelirleme)
DeterjanMiktari.view(sim=MakinaBelirleme)
AltPompaDevri.view(sim=MakinaBelirleme)