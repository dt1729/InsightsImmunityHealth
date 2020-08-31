import pandas as pd
import numpy as np
import scipy

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
# give this function numpy data input
def findingDaysfromWeek(week_num,insightDuration,daily_data):
    # week start should be a multiple of 7 or 0
    # might have to make it week_num - 1 if the year is normal currently leap year so week_num-2
    if week_num < 100:
        week_start = 7*(week_num-1)
    else:
        week_start = 7*(week_num-2)
    return daily_data[week_start:week_start+7*insightDuration]['Steps'], daily_data[week_start:week_start+7*10]['Steps']

# combining this with 
def findingDaysfromWeek(week_num,insightDuration,daily_data):
    # week start should be a multiple of 7 or 0
    # might have to make it week_num - 1 if the year is normal currently leap year so week_num-2
    if week_num < 100:
        week_start = 7*(week_num-1)
    else:
        week_start = 7*(week_num-2)
    return daily_data[week_start:week_start+7*insightDuration]['Steps'], daily_data[week_start:week_start+7*10]['Steps']
# combining this with 
def setofInsightMonthly(steps_week,threeWeek = False,twoWeek = False):
#   THIS FUNCTION FINDS and STORES THE INSIGHTS ON THE BASIS OF A 4WEEK/28DAY PERIOD 
#   ALSO FINDS ON THE BASIS OF 3 and 2 weeks
    steps_week_np = steps_week.to_numpy()
    temp = steps_week_np[len(steps_week_np)-12:len(steps_week_np)-1]
#     steps_12week = np.flip(steps_week_np[len(steps_week_np)-12:len(steps_week_np)],axis = 0) #flipping the last to the first for easier access to indices 
    steps_12week = steps_week_np[len(steps_week_np)-12:len(steps_week_np)-1]
    weeknum = np.unique([steps_12week[i][0] for i in range(0,len(steps_12week))]) #finding unique week numbers from which insights need to be extracted
    print(weeknum)
    sliding_insight_four_week = {'mean':np.zeros(len(steps_12week) - 3),'stdDev':np.zeros(len(steps_12week) - 3),'weeknum':[]} #hardcoded sliding possibilities according to a month
    sliding_insight_three_week = {'mean':np.zeros(len(steps_12week) - 2),'stdDev':np.zeros(len(steps_12week) - 2),'weeknum':[]}
    sliding_insight_two_week = {'mean':np.zeros(len(steps_12week) - 1),'stdDev':np.zeros(len(steps_12week) - 1),'weeknum':[]}
#     finding mean of Grouped weekly 
    sliding_insight_four_week['mean'] = [np.mean(steps_12week[i:i+4,1]) for i in range(0,len(steps_12week)-3)]
    sliding_insight_four_week['weeknum'] = [weeknum[i:i+4][0] for i in range(0,len(steps_12week)-3)]
#     print(sliding_insight_four_week['weeknum'])
    if threeWeek:
        sliding_insight_three_week['mean'] = [np.mean(steps_12week[i:i+3,1]) for i in range(0,len(steps_12week)-2)]
        sliding_insight_three_week['weeknum'] = [weeknum[i:i+3][0] for i in range(0,len(steps_12week)-2)]
    if twoWeek:
        sliding_insight_two_week['mean'] = [(np.mean(steps_12week[i:i+2,1])) for i in range(0,len(steps_12week)-1)]
        sliding_insight_two_week['weeknum'] = [weeknum[i:i+2][0] for i in range(0,len(steps_12week)-1)]
    return sliding_insight_four_week,sliding_insight_three_week,sliding_insight_two_week
# CAN USE THIS OR STUDENT'S T TEST
def tTest(data1,data2,alpha):
    # calculate means
    data1 = data1.to_numpy()
    data2 = data2.to_numpy()
    mean1, mean2 = np.mean(data1), np.mean(data2)
    # number of paired samples
    n1 = len(data1)
    n2 = len(data2)
    # sum squared difference between observations
    s1 = np.std(data1)**2
    # sum difference between observations
    s2 = np.std(data2)**2
    # standard deviation of the difference between means
    den = np.sqrt(s1/len(data1) + s2/len(data2))
    # standard error of the difference between the means
    num = (mean1 - mean2)
    # calculate the t statistic
    t_stat = abs(num/den)
    # degrees of freedom
    df = ((s1**2/n1) + (s2**2/n2))**2/((s1**2/n1)**2/(n1-1) + (s2**2/n2)**2/(n2-1))
    # calculate the critical value
    cv = scipy.stats.t.ppf(1.0 - alpha, df)
    # calculate the p-value
    p = (1.0 - scipy.stats.t.cdf(abs(t_stat), df)) * 2.0
    return t_stat, df, cv, p
    # return everything
#     return data2


def gettingInsights():
    steps_per_day,steps_per_week = csv_to_pd()
#     print(steps_per_day)
    dict4week,dict3week,dict2week = setofInsightMonthly(steps_per_week,threeWeek = True,twoWeek = True)
#     print(dict4week['weeknum'])
    weekconsidered = 233
    insight2week,meandiff2week = weekInsight(weekconsidered,steps_per_day,dict2week,2)
    insight3week,meandiff3week = weekInsight(weekconsidered,steps_per_day,dict3week,3)
    insight4week,meandiff4week = weekInsight(weekconsidered,steps_per_day,dict4week,4)
    weekNo2week,maxdiff2week = printGroupedInsightsHelper(insight2week,meandiff2week)
    weekNo3week,maxdiff3week = printGroupedInsightsHelper(insight3week,meandiff3week)
    weekNo4week,maxdiff4week = printGroupedInsightsHelper(insight4week,meandiff4week)
    if printGroupInsight(weekNo2week,meandiff2week,insight2week):
        print(maxdiff2week)
        print(weekNo2week)
    else:
        print('Please keep up your walking your performance went down from week '+str(weekNo2week)+' to '+str(weekNo2week+1)+' by '+str(maxdiff2week)+' on average')
    print(maxdiff3week)
    print(maxdiff4week)
    print(weekNo3week)
    print(weekNo4week)
def weekInsight(weekconsidered,steps_per_day,WeekgroupedData,groupSize):
    dailydatanumpy1,dailydata12week = findingDaysfromWeek(weekconsidered,groupSize,steps_per_day)
    a = np.array(WeekgroupedData['weeknum'])
    weekIndexGrouped = list(np.where(a == weekconsidered))
#     print(weekIndexGrouped[0])
#     print(WeekgroupedData['weeknum'])
    if len(weekIndexGrouped[0]) == 0:
        insight = []
        meandiff = []
        return insight,meandiff
    weekIndex = int(weekIndexGrouped[0])
    insight = []
    meandiff = []
    for i in range(0,len(WeekgroupedData['weeknum'])):
        dailydatanumpy2,_ = findingDaysfromWeek(WeekgroupedData['weeknum'][i],groupSize,steps_per_day)
        t_stat,_,_,p =  tTest(dailydatanumpy1,dailydatanumpy2,0.05)
        if t_stat > p and weekIndex > i:
            insight.append(WeekgroupedData['weeknum'][i])
            meandiff.append(WeekgroupedData['mean'][weekIndex] - WeekgroupedData['mean'][i])
    # two 4 week insight comparison
    return insight,meandiff
def printGroupedInsightsHelper(insight,meandiff):
    meandiffabs = [abs(number) for number in meandiff]
    print(meandiffabs)
    maxdiff = np.amax(meandiffabs)
    index = np.where(meandiffabs == maxdiff)
    return insight[int(index[0])],meandiffabs[int(index[0])]
def printGroupInsight(insightweek,meandiff,weeknum):
    indexInsight = np.where(weeknum == insightweek)
    if meandiff[int(indexInsight[0])] > 0:
        return True
    else:
        return False


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