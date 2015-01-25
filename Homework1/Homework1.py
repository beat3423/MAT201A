
# coding: utf-8

# In[1]:

# MAT 201A Media Signal Processing Homework 1
# Intae Hwang Jan 20 2015

# Source Code originated from
# https://www.youtube.com/watch?v=95qb1_pEV-g by sentdex
# "How to Graph in Python From a CSV Spreadsheet (Dates included)"   

# Data source "Exchange rate Korean Won to Us dollar, Japan Yen, and Euro.
# http://info.finance.naver.com/marketindex/exchangeDetail.nhn?marketindexCd=FX_USDKRW // US
# http://info.finance.naver.com/marketindex/exchangeDetail.nhn?marketindexCd=FX_JPYKRW // Japan
# http://info.finance.naver.com/marketindex/exchangeDetail.nhn?marketindexCd=FX_EURKRW // Euro


# In[2]:

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


# In[3]:

get_ipython().magic(u'pylab inline')


# In[4]:

dict(alpha=0.5, edgecolor='none')


# In[47]:

def graph():
    date, us, japan, euro = np.loadtxt('/Users/intaehwang/Desktop/project2/python/ass/exchange7.csv',
                              delimiter=',', unpack=True, converters = {0:
                              mdates.strpdate2num('%Y-%m-%d')})
    fig = plt.figure()
    
    
    
    ax1 = fig.add_subplot(1,1,1, axisbg='white')
    plt.plot_date(x=date, y=us, fmt='o-')
    ax1.set_xticks(date)
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%m/%d'))
    
    ax2 = fig.add_subplot(1,1,1, axisbg='white')
    plt.plot_date(x=date, y=japan, fmt='o-')
    
    ax3 = fig.add_subplot(1,1,1, axisbg='white')
    plt.plot_date(x=date, y=euro, fmt='o-')
   
    names = ['US (Dollar)', 'Japan (Yen)', 'EU (Euro)']
    legend(names,bbox_to_anchor=(1.35,1),loc=1, borderaxespad=0.)
    
    plt.suptitle('Exchange Rate Changes "Won" in Korea from 2015-01-05 to 2015-01-16', 
                 fontsize =15, fontweight='bold', x=0.60, y=1.08)
    
    plt.ylim(870,1350)
     
    plt.ylabel('rate (Won)', fontsize=15)
    plt.xlabel('date', fontsize=15)
     
    #fig.autofmt_xdate(rotation=25)
    fig.tight_layout()

    
    plt.grid(True)
    plt.savefig('homework1_intae.png', bbox_inches='tight', pad_inches=1) 
    plt.show()
      
   
graph()


# In[ ]:



