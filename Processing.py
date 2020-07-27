import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def loadData():
    data = pd.read_csv('E:\\Document\\Kagge\\Quevico\\data_all\\train.csv')
    exRate = pd.read_csv('E:\\Document\\Kagge\\Quevico\\data_all\\rate.csv')
    return data, exRate


def processSalary(data, exRate):
    exRate = pd.Series(exRate.USD.values, index = exRate.Country).to_dict()
    data['rate'] = data['CurrencySymbol'].map(exRate)
    data['ConvertSalary'] = data['Salary']*data['rate']
    return data

def processCompanySize(data):
    company_size = {'Fewer than 10 employees' : 0,
                    '10 to 19 employees'      : 1,
                    '20 to 99 employees'      : 2,
                    '100 to 499 employees'    : 3,
                    '500 to 999 employees'    : 4,
                    '1,000 to 4,999 employees': 5,
                    '5,000 to 9,999 employees': 6,
                    '10,000 or more employees': 7
                    }
    data['CompanySize'] = data['CompanySize'].map(company_size)
    return data

def processSalaryType(data):
    salary_type = {'Weekly' : 4*12,
                   'Monthly': 12,
                   'Yearly' : 1
                   }
    data['ProcessSalaryType'] = data['SalaryType'].map(salary_type)
    data['ProcessSalaryType'].fillna(1)
    return data

def processEmployment(data):
    employment = {'Employed full-time' : 0,
                  'Employed part-time' : 1,
                  'Independent contractor, freelancer, or self-employed' : 2,
                  'Not employed, and not looking for work' : 3,
                  'Not employed, but looking for work' : 4
                  }
    data['Employment'] = data['Employment'].map(employment)
    return data

def processFormalEdu(data):
    formalEdu = {'I never completed any formal education' : 0,
                 'Primary/elementary school' : 1,
                 'Secondary school (e.g. American high school, German Realschule or Gymnasium, etc.)' : 2,
                 'Some college/university study without earning a degree' : 3,
                 'Associate degree' : 4,
                 'Professional degree (JD, MD, etc.)': 5,
                 "Bachelor's degree (BA, BS, B.Eng., etc.)" : 6,
                 "Master's degree (MA, MS, M.Eng., MBA, etc.)" : 7,
                 "Other doctoral degree (Ph.D, Ed.D., etc.)" :8
                 }
    data['FormalEducation'] = data['FormalEducation'].map(formalEdu)

def processMajor(data):
    major = {'A business discipline (ex. accounting, finance, marketing)':0,
             'A health science (ex. nursing, pharmacy, radiology)' : 1,
             'A humanities discipline (ex. literature, history, philosophy)' : 2,
             'A natural science (ex. biology, chemistry, physics)' : 3,
             'A social science (ex. anthropology, psychology, political science)':4,
             'Another engineering discipline (ex. civil, electrical, mechanical)':5,
             'Computer science, computer engineering, or software engineering':6,
             'Fine arts or performing arts (ex. graphic design, music, studio art)':7,
             'I never declared a major':8,
             'Information systems, information technology, or system administration':9,
             'Mathematics or statistics':10,
             'Web development or web design':11
             }
    data['UndergradMajor'] = data['UndergradMajor'].map(major)
    return data

