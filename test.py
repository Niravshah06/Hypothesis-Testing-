
from xlrd import open_workbook
from src.bean import Bean
from scipy import stats
import math
import numpy as np

    

#step1 import data and store it in bean
wb = open_workbook('data.xlsx')
for sheet in wb.sheets():
    number_of_rows = sheet.nrows
    number_of_columns = sheet.ncols

    items = []

    rows = []
    for row in range(1, number_of_rows):
        values = []
        for col in range(number_of_columns):
                value  = (sheet.cell(row,col).value)
                values.append(value)
        item = Bean(*values)
        items.append(item)


#step 2 find means
HDLCwithCVD = [];
LDLCwithCVD =[];

HDLCwithoutCVD= []
LDLCwithoutCVD= []
  
nforCVD=0 
nWithoutCVD=0
 
for i in items:
    if(i.CVD==0):
        nWithoutCVD=nWithoutCVD+1;
        HDLCwithoutCVD.append(i.HDLC)
        LDLCwithoutCVD.append(i.LDLC)
    else:
        
        HDLCwithCVD.append(i.HDLC)
        LDLCwithCVD.append(i.LDLC)
        nforCVD=nforCVD+1
  

meanHDLCwithCVD=sum(HDLCwithCVD)/nforCVD
meanLDLCWithCVD=sum(LDLCwithCVD)/nforCVD;

meanHDLCwithoutCVD=sum(HDLCwithoutCVD)/nWithoutCVD;
meanLDLCwithoutCVD=sum(LDLCwithoutCVD)/nWithoutCVD;

print("Null Hypothesis testing using t-test\n")

print('mean with cvd for HDLD ',meanHDLCwithCVD)
print('mean with cvd for LDLD ',meanLDLCWithCVD)
print('mean with cvd for HDLD ',meanHDLCwithoutCVD)
print('mean without cvd for LDLC ' ,meanLDLCwithoutCVD,'\n\n')
#step3 do null hypothesis

#########now test for ldl without cvd as sample agaonst know mean of LDL with CVD
print("testing ldl starts\n")
#t test 1 
print('test1\n testing ldlcwithoutcvd as sample  and giving ldlcwithCVD as known mean')
print(stats.ttest_1samp(LDLCwithoutCVD,meanLDLCWithCVD))
xtemp=stats.ttest_1samp(LDLCwithoutCVD,meanLDLCWithCVD).__getattribute__('statistic')
pvalue1=stats.ttest_1samp(LDLCwithoutCVD,meanLDLCWithCVD).__getattribute__('pvalue')


print('chances of seeing a result as extreme',stats.t.cdf(x= xtemp,df=49)*2)
#give 0.07.> 0.05 thus LDLC without CVD is true

#since there is a 1.83% chance of seeing a result this extreme due to chance,
# it is not significant at the 99% confidence level. 
#This means if we were to construct a 95% confidence interval, it would capture the ldl with cvd mean

#fins ==d standard deviation and scale
sigma = np.std(LDLCwithoutCVD)/math.sqrt(len(items))

print('data distribution',stats.t.interval(0.95,                        # Confidence level
                 df = 49,                     # Degrees of freedom
                 loc = meanLDLCwithoutCVD, # Sample mean
                 scale= sigma))



#########now test for ldl with cvd as sample agaonst know mean of LDL without CVD
#t test 2
print('\ntest2\ntesting ldlcwithtcvd as sample  and giving ldlcwithoutCVD as known mean')
print(stats.ttest_1samp(LDLCwithCVD,meanLDLCwithoutCVD))
xtemp=stats.ttest_1samp(LDLCwithCVD,meanLDLCwithoutCVD).__getattribute__('statistic')
pvalue2=stats.ttest_1samp(LDLCwithCVD,meanLDLCwithoutCVD).__getattribute__('pvalue')

#this give same p values as when we did t test
print('chances of seeing a result as extreme',stats.t.cdf(x= xtemp,df=49)*2)
#give 1.9.> 0.05 thus LDLC without CVD is true

#fins ==d standard deviation and scale
sigma = np.std(LDLCwithCVD)/math.sqrt(len(items))

print('data distribution',stats.t.interval(0.95,                        # Confidence level
                 df = 49,                     # Degrees of freedom
                 loc = meanLDLCWithCVD, # Sample mean
                 scale= sigma))

#as we can see that in bith case p values is greater than 0.05 thus both group data are same and we cant reject null hypothesis


if(pvalue1>0.05 and  pvalue2>0.05):
    print('\nTest Result :since in both test  the p-value of  is greater than our significance level of 0.05 and we fail to reject the null hypothesis.')
else:
    print("\nTest Result: we reject the null hypothesis")
print("\n testing hdl starts")


#t test 3
print('\ntest3\ntesting HDLCwithoutCVD as sample  and giving HDLCwithCVD as known mean')

print(stats.ttest_1samp(HDLCwithoutCVD,meanHDLCwithCVD))
xtemp=stats.ttest_1samp(HDLCwithoutCVD,meanHDLCwithCVD).__getattribute__('statistic')
pvalue3=stats.ttest_1samp(HDLCwithoutCVD,meanHDLCwithCVD).__getattribute__('pvalue')



print('chances of seeing a result as extreme',stats.t.cdf(x= xtemp,df=49)*2)
#give 0.07.> 0.05 thus LDLC without CVD is true

#since there is a 1.83% chance of seeing a result this extreme due to chance,
# it is not significant at the 99% confidence level. 
#This means if we were to construct a 99% confidence interval, it would capture the ldl with cvd mean

#fins ==d standard deviation and scale
sigma = np.std(HDLCwithoutCVD)/math.sqrt(len(items))

print('data distribution',stats.t.interval(0.95,                        # Confidence level
                 df = 49,                     # Degrees of freedom
                 loc = meanHDLCwithoutCVD, # Sample mean
                 scale= sigma))
# it covers the 

if(pvalue3>0.05):
    print('\nTest Result :since in both test  the p-value of  is greater than our significance level of 0.05 and we fail to reject the null hypothesis.')

else:
    print("\nTest Result: we reject the null hypothesis")



