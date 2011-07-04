day_of_month=7 
month="january"
year=1900
number_of_sundays=0

def increment_year():
    global year
    year+=1
    
def increment_month():
    global month
    if(month=="january"):
        month="february"
    elif(month=="february"):
        month="march"
    elif(month=="march"):
        month="april"
    elif(month=="april"):
        month="may"
    elif(month=="may"):
        month="june"
    elif(month=="june"):
        month="july"
    elif(month=="july"):
        month="august"
    elif(month=="august"):
        month="september"
    elif(month=="september"):
        month="october"
    elif(month=="october"):
        month="november"
    elif(month=="november"):
        month="december"
    else:
        increment_year()
        month="january"
        
def is_year_leap():
    global year
    if(year%4==0):
        if(year%100==0 and year%400!=0):
            return False
        else:
            return True
    else:
        return False

def generate_next_sunday():
    global day_of_month
    global number_of_sundays
    while(year<2001):
        day_of_month+=7
        if(month=='january' or month=='march' or month=='may' or month=='july' or month=='august' or month=='october' or month=='december'):
            if(day_of_month>31):
                day_of_month=day_of_month-31
                increment_month()
        elif(month=='april' or month=='june' or month=='september' or month=='november'):
            if(day_of_month>30):
                day_of_month=day_of_month-30
                increment_month()
        else:
            if(is_year_leap()):
                if(day_of_month>29):
                    day_of_month=day_of_month-29
                    increment_month()
            else:
                if(day_of_month>28):
                    day_of_month=day_of_month-28
                    increment_month()
        if(day_of_month==1 and year>1900):
            number_of_sundays+=1
        
generate_next_sunday()
print "Number of Sundays that fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000) are "+str(number_of_sundays)
