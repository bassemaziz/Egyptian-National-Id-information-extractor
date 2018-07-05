from datetime import datetime
from dateutil import relativedelta

id = "21609162300316"


def getDate(id):
    """
    Internal function
    """
    M = id[3:5]
    D = id[5:7]
    if id[0]=="2":
        Y=str(19)+id[1:3]
    if id[0]=="3":
        Y=str(20)+id[1:3]
    year = str(Y)
    month = str(M)
    day = str(D)
    return year,month,day


def getDateOfBirth(id):
    """
    return format string "yyy/mm/dd"
    """
    y,m,d=getDate(id)
    return(y+'/'+m+'/'+d)


def getAgeOnFirstOfOctober(id):
    """
    return years  :
        getAgeOnFirstOfOctober(id)[0] 
    return months :
        getAgeOnFirstOfOctober(id)[1] 
    return days   :
        getAgeOnFirstOfOctober(id)[2]  
     
    """
    y,m,d=getDate(id)
    dateOfBirth =  datetime(int(y),int(m),int(d),00,00)
    yearOfTheYear = datetime.today().strftime("%Y")
    difference = relativedelta.relativedelta(datetime(int(yearOfTheYear),10,1,00,00),dateOfBirth)
    years = difference.years
    months = difference.months
    days = difference.days
    return str(years),str(months),str(days)


def getStageBasedOnAge(id):
    """
    return is aged false or ture as bolian type :
        getStageBasedOnAge(id)[0]
    return stage as string :
        getStageBasedOnAge(id)[0]

    """
    y,m,d=getAgeOnFirstOfOctober(id)
    stages=["kg1","kg2","first","classOne"]
    isAged= True
    stage="not meeting requirements"
    if int(y)>=4 and int(y)<=15:
        if int(y)>=9 and int(y)<=15:
            stage=stages[3]
        if float(y)>=4 and float(m) <= 9:
                stage=stages[0]
        if float(y)>=5 and float(m) <= 9:
                stage=stages[1]
        if float(y)>=6 and float(m) <= 9:
                stage=stages[2]
    else :
        isAged= False
    return isAged,str(stage)


def getDateOfRetirement(id):
    """
    return format string "yyy/mm/dd"
    """
    yearOfTheYear = datetime.today().strftime("%Y")   
    y,m,d=getDate(id)
    difference = int(yearOfTheYear) - int(y)
    
    if not difference >60 :
        Y=int(y)+60
    else:
        return "OnRetirementAge"
    
    return(str(Y)+'/'+m+'/'+d)


def getGovName(id):
    """ 
        return name of gov :
            getGovName(id)[0]) 
        return cod of gov as string 
            getGovName(id)[1])
    """
    govCods={    
        "01":"القاهرة",
        "02":"الإسكندرية",
        "03":"بورسعيد",
        "04":"السويس",
        "11":"دمياط",
        "12":"الدقهلية",
        "13":"الشرقية",
        "14":"القليوبية",
        "15":"كفر الشيخ",
        "16":"الغربية",
        "17":"المنوفية",
        "18":"البحيرة",
        "19":"الإسماعيلية",
        "21":"الجيزة",
        "22":"بني سويف",
        "23":"الفيوم",
        "24":"المنيا",
        "25":"أسيوط",
        "26":"سوهاج",
        "27":"قنا",
        "28":"أسوان",
        "29":"الأقصر",
        "31":"البحر الأحمر",
        "32":"الوادى الجديد",
        "33":"مطروح",
        "34":"شمال سيناء",
        "35":"جنوب سيناء",
        "88":"خارج الجمهورية"}
    return govCods[id[7:9]],id[7:9]

def getGender(id):
    """
    return gender as string (femail/mail)
    """
    if int(id[12:13])%2==0:
        return "femail"
    else:
        return "male"


print("-----------------------------------------------------")
print("Date of birth : "+ getDateOfBirth(id))
print("Gender is : "+ getGender(id))
print("Place of birth : "+ getGovName(id)[0])
print("Date of retairment : "+ getDateOfRetirement(id))
print("-----------------------------------------------------")
print("Age on first of october is :")
print(getAgeOnFirstOfOctober(id))
print("Stage of Age ")
print(getStageBasedOnAge(id))
print("-----------------------------------------------------")

