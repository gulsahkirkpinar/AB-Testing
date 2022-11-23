# -*- coding: utf-8 -*-

# -- Sheet --

#Bir firmanın web site bilgilerini içeren bu veri setinde kullanıcıların gördükleri ve tıkladıkları reklam sayıları gibi bilgilerin yanı sıra 
#buradan gelen kazanç bilgileri yer almaktadır. Kontrol ve Test grubu olmak üzere iki ayrı veri seti vardır. Bu veri setleri
#ab_testing.xlsx excel’inin ayrı sayfalarında yer almaktadır. Kontrol grubuna Maximum Bidding, test grubuna Average
#Bidding uygulanmıştır

###GÖREV1 Veriyi Hazırlama ve Analiz Etme

#Adım 1: ab_testing_data.xlsx adlı kontrol ve test grubu verilerinden oluşan veri setini okutunuz. Kontrol ve test grubu verilerini ayrı 
#değişkenlere atayınız.
#Adım 2: Kontrol ve test grubu verilerini analiz ediniz.
#Adım 3: Analiz işleminden sonra concat metodunu kullanarak kontrol ve test grubu verilerini birleştiriniz.

!pip install statsmodels
!pip install openpyxl

import itertools
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#!pip install statsmodels
import statsmodels.stats.api as sms
from scipy.stats import ttest_1samp, shapiro, levene, ttest_ind, mannwhitneyu, \
    pearsonr, spearmanr, kendalltau, f_oneway, kruskal
from statsmodels.stats.proportion import proportions_ztest

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 10)
pd.set_option('display.float_format', lambda x: '%.5f')

###Adım2

df_control = pd.read_excel("ab_testing.xlsx", sheet_name="Control Group")

df_test = pd.read_excel("ab_testing.xlsx", sheet_name="Test Group")

df_control.info()

df_control.head()

df_test.head()

df_control.isnull().sum()
df_test.isnull().sum()
df_test.describe().T
df_control.describe().T

###Adım3

display(pd.concat([df_control, df_test]))

###Görev2


##Adım 1

##Hipotezi tanımlayınız.
##H0 : M1 = M2 
##H1 : M1 != M2

#Adım 2: Kontrol ve test grubu için purchase (kazanç) ortalamalarını analiz ediniz

test_stat, pvalue = shapiro(df_test["Purchase"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))


test_stat, pvalue = shapiro(df_control["Purchase"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

##p-value > 0.05 olduğu için H0 reddedilmez.Normallik varsayımı sağlanmıştır.
# Varsayımlar sağlanıyorsa bağımsız iki örneklem t testi (parametrik test) kullanılacak.

test_stat, pvalue = ttest_ind(df_test["Purchase"],
                              df_control["Purchase"],
                              equal_var=True)
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

##p-value> 0.05 olduğu için H0 kabul edilir.

##O halde iki durum arasında istatistiksel olarak anlamlı bir fark yoktur.İlk aşamada bakıldığında ortalamalar arasında fark var gibi görünse de bu farkın tesadüfi olduğunu görmüş olduk.
 ##Yapılan değişiklik herhangi bir fayda sağlayacak gibi görünmüyor.Geliştirme yapılmalıdır.

