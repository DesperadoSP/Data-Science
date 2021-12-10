#Edwin Zhu
#Edwin.Zhu13@myhunter.cuny.edu
#Title: Covid-19 Trends and why they occur
#Resources: https://www.ajmc.com/view/a-timeline-of-covid19-developments-in-2020, https://www.hopkinsmedicine.org/health/conditions-and-diseases/coronavirus/first-and-second-waves-of-coronavirus, https://en.wikipedia.org/wiki/Boroughs_of_New_York_City
#URL: https://edwinzhu595.wixsite.com/website
#Data Sources: https://data.cityofnewyork.us/Health/COVID-19-Daily-Counts-of-Cases-Hospitalizations-an/rc75-m7u3
              #Taken straight from the data source: "Daily count of NYC residents who tested positive for SARS-CoV-2, who were hospitalized with COVID-19, and deaths among COVID-19 patients."
              #Exported as a csv
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

yes = pd.read_csv("data.csv")
yes['ord_date']= pd.to_datetime(yes['DATE_OF_INTEREST']) 

#Case count: Shows graph of positive test cases from February 2020 till present day for NYC.
def case_count():
    result = yes.groupby([yes['ord_date'].dt.year, yes['ord_date'].dt.month]).agg({'CASE_COUNT':sum}).plot.bar(legend='')
    plt.title('Case counts from February 2020 to Present Day')
    plt.xlabel('Date')
    plt.ylabel('Case Count')
    plt.xticks(fontsize=5.5)
    plt.show()

#Hospitalized count: Shows graph of hospitalizations from February 2020 till present day for NYC.
def hospitalized_count():
    result = yes.groupby([yes['ord_date'].dt.year, yes['ord_date'].dt.month]).agg({'HOSPITALIZED_COUNT':sum}).plot.bar(legend='')
    plt.title('Hospitalized counts from Feb 2020 to Present Day')
    plt.xlabel('Date')
    plt.ylabel('Hospitalized Count')
    plt.xticks(fontsize=5.5)
    plt.show()

#Death count: Shows graph of deaths from February 2020 till present day for NYC.
def death_count():
    result = yes.groupby([yes['ord_date'].dt.year, yes['ord_date'].dt.month]).agg({'DEATH_COUNT':sum}).plot.bar(legend='')
    plt.title('Death counts from Feb 2020 to Present Day')
    plt.xlabel('Date')
    plt.ylabel('Death Count')
    plt.xticks(fontsize=5.5)
    plt.show()

#Borough case count: Shows graph of positive test cases for all 5 boroughs of NYC from February 2020 till present day.
def borough_case_count():
    test = yes.groupby([yes['ord_date'].dt.year, yes['ord_date'].dt.month]).agg(
               BX=pd.NamedAgg(column="BX_CASE_COUNT", aggfunc="sum"),
               BK=pd.NamedAgg(column="BK_CASE_COUNT", aggfunc="sum"),                             
               MN=pd.NamedAgg(column="MN_CASE_COUNT", aggfunc="sum"),     
               QN=pd.NamedAgg(column="QN_CASE_COUNT", aggfunc="sum"),
               SI=pd.NamedAgg(column="SI_CASE_COUNT", aggfunc="sum"))     
    test1 = test.plot.bar()   
    plt.title('Case counts of each borough from Feb 2020 to Present Day')      
    plt.xlabel('Date')
    plt.ylabel('Case Count')
    plt.xticks(fontsize=5.5)
    plt.show()

#Borough hospitalized count: Shows graph of hospitalizations for all 5 boroughs of NYC from February 2020 till present day.
def borough_hospitalizated_count():
    test = yes.groupby([yes['ord_date'].dt.year, yes['ord_date'].dt.month]).agg(
               BX=pd.NamedAgg(column="BX_HOSPITALIZED_COUNT", aggfunc="sum"),
               BK=pd.NamedAgg(column="BK_HOSPITALIZED_COUNT", aggfunc="sum"),                             
               MN=pd.NamedAgg(column="MN_HOSPITALIZED_COUNT", aggfunc="sum"),     
               QN=pd.NamedAgg(column="QN_HOSPITALIZED_COUNT", aggfunc="sum"),
               SI=pd.NamedAgg(column="SI_HOSPITALIZED_COUNT", aggfunc="sum"))     
    test1 = test.plot.bar()   
    plt.title('Hospitalized counts of each borough from Feb 2020 to Present Day')      
    plt.xlabel('Date')
    plt.ylabel('Hospitalized Count')
    plt.xticks(fontsize=5.5)
    plt.show()

#Borough death count: Shows graph of deaths for all 5 boroughs of NYC from February 2020 till present day.
def borough_death_count():
    test = yes.groupby([yes['ord_date'].dt.year, yes['ord_date'].dt.month]).agg(
               BX=pd.NamedAgg(column="BX_DEATH_COUNT", aggfunc="sum"),
               BK=pd.NamedAgg(column="BK_DEATH_COUNT", aggfunc="sum"),                             
               MN=pd.NamedAgg(column="MN_DEATH_COUNT", aggfunc="sum"),     
               QN=pd.NamedAgg(column="QN_DEATH_COUNT", aggfunc="sum"),
               SI=pd.NamedAgg(column="SI_DEATH_COUNT", aggfunc="sum"))     
    test1 = test.plot.bar()   
    plt.title('Death counts of each borough from Feb 2020 to Present Day')      
    plt.xlabel('Date')
    plt.ylabel('Death Count')
    plt.xticks(fontsize=5.5)
    plt.show()
 
#I have decided to drop the predictive modeling due to time constraint, plus the fact that it would lead to a success metric that is not realizable by the end of the semester.
#Predictive Modeling
#result = yes.groupby([yes['ord_date'].dt.year, yes['ord_date'].dt.month]).agg({'CASE_COUNT':sum}).plot.bar(legend='')
