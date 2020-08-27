import pandas as pd
import numpy as np

def csv_to_pd():
    steps_per_day = pd.read_csv('steps_per_day_shashank.csv')
    steps_per_week = pd.read_csv('steps_per_week_shashank.csv')
    return steps_per_day,steps_per_week

def weeklyInsights(df_week):
    weeklyChanges = np.zeros_like(df_week['Steps'])
    for i in range(1,len(weeklyChanges)):
        weeklyChanges[i] = df_week['Steps'][i] - df_week['Steps'][i-1]

def dailyInsights(df_day):
    dailyChanges = np.zeros_like(df_day['Steps'])
    for i in range(1,len(weeklyChanges)):
        weeklyChanges[i] = df_day['Steps'][i] - df_day['Steps'][i-1]
# combining this with 
def setofInsightMonthly(steps_week,steps_days,threeWeek = False,twoWeek = False):
#   THIS FUNCTION FINDS and STORES THE INSIGHTS ON THE BASIS OF A 4WEEK/28DAY PERIOD 
#   ALSO FINDS ON THE BASIS OF 3 and 2 weeks
    steps_week_np = steps_week.to_numpy()
    steps_12week = np.flip(steps_week_np[len(steps_week_np)-13:len(steps_week_np)-2],axis = 0) #flipping the last to the first for easier access to indices 
    sliding_insight_four_week = np.zeros(len(steps_12week) - 5) #hardcoded sliding possibilities according to a month
    sliding_insight_three_week = np.zeros(len(steps_12week) - 4)
    sliding_insight_two_week = np.zeros(len(steps_12week) - 3)
#     finding mean of Grouped weekly data
    sliding_insight_four_week = [np.mean(steps_12week[i:i+4,1]) for i in range(0,len(steps_12week)-5)]
    if threeWeek:
        sliding_insight_three_week = [np.mean(steps_12week[i:i+3,1]) for i in range(0,len(steps_12week)-4)]
    if twoWeek:
        sliding_insight_two_week = [np.mean(steps_12week[i:i+2,1]) for i in range(0,len(steps_12week)-3)]
    return sliding_insight_four_week,sliding_insight_three_week,sliding_insight_two_week
# CAN USE THIS OR STUDENT'S T TEST
def gaussianModel(mean,variance)
    return 
# 

def printInsight(start, end, daily = False, weekly = False):
    dailyData,weeklyData = csv_to_pd()
    if daily:
        day1 = dailyData['Steps'][start]
        day2 = dailyData['Steps'][end]
        dailychange = day1 - day2
        percent = lambda x,y: str(((x-y)/x)*100)
        if dailychange < 0:
            print('Your cardio has dropped by '+str(abs(dailychange))+' steps please keep walking')
        else:
            print('Your walking increased by '+str(dailychange)+' steps good job!')
    elif weekly:
        week1 = weeklyData['Steps'][start]
        week2 = weeklyData['Steps'][end]
        weeklychange = week1 - week2
        percent = lambda x,y: str((x-y/x)*100)
        if weeklychange < 0:
            print('Your cardio has dropped by '+str(abs(weeklychange))+' steps this week please keep walking')
        else:
            print('Your walking increased by '+str(weeklychange)+' steps this week good job!')


if __name__ == "__main__":
    print('This is shashank\'s walking data \n')
    # this can be converted into API and the data can be taken as input to a POST call
    daily1 = True
    weekly1 = False
    starting = 2
    ending = 3
    printInsight(starting,ending,daily1,weekly1)