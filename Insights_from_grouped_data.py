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
    week_start = 7*(week_num-2)
    return daily_data[week_start:week_start+7*insightDuration][2]
# combining this with 
def setofInsightMonthly(steps_week,threeWeek = False,twoWeek = False):
#   THIS FUNCTION FINDS and STORES THE INSIGHTS ON THE BASIS OF A 4WEEK/28DAY PERIOD 
#   ALSO FINDS ON THE BASIS OF 3 and 2 weeks
    steps_week_np = steps_week.to_numpy()
    steps_12week = np.flip(steps_week_np[len(steps_week_np)-13:len(steps_week_np)-2],axis = 0) #flipping the last to the first for easier access to indices 
    sliding_insight_four_week = {'mean':np.zeros(len(steps_12week) - 4),'stdDev':np.zeros(len(steps_12week) - 4),'weeknum':steps_week_np[0][0]} #hardcoded sliding possibilities according to a month
    sliding_insight_three_week = {'mean':np.zeros(len(steps_12week) - 3),'stdDev':np.zeros(len(steps_12week) - 3),'weeknum':steps_week_np[0][0]}
    sliding_insight_two_week = {'mean':np.zeros(len(steps_12week) - 2),'stdDev':np.zeros(len(steps_12week) - 2),'weeknum':steps_week_np[0][0]}
#     finding mean of Grouped weekly data
    sliding_insight_four_week['mean'] = [np.mean(steps_12week[i:i+4,1]) for i in range(0,len(steps_12week)-4)]
    if threeWeek:
        sliding_insight_three_week['mean'] = [np.mean(steps_12week[i:i+3,1]) for i in range(0,len(steps_12week)-3)]
    if twoWeek:
        sliding_insight_two_week['mean'] = [(np.mean(steps_12week[i:i+2,1])) for i in range(0,len(steps_12week)-2)]
    return sliding_insight_four_week,sliding_insight_three_week,sliding_insight_two_week
# CAN USE THIS OR STUDENT'S T TEST
def tTest(data1,data2,alpha):
	# calculate means
	mean1, mean2 = mean(data1), mean(data2)
	# number of paired samples
	n1 = len(data1)
    n2 = len(data2)
	# sum squared difference between observations
	sp = np.std(data1)**2
	# sum difference between observations
	s2 = np.std(data2)**2
	# standard deviation of the difference between means
	den = np.sqrt(s1/len(data1) + s2/len(data2))
	# standard error of the difference between the means
	num = (mean1 - mean2)
	# calculate the t statistic
	t_stat = num/den
	# degrees of freedom
	df = ((s1**2/n1) + (s2**2/n2))**2/((s1**2/n1)**2/(n1-1) + (s2**2/n2)**2/(n2-1))
	# calculate the critical value
	cv = t.ppf(1.0 - alpha, df)
	# calculate the p-value
	p = (1.0 - t.cdf(abs(t_stat), df)) * 2.0
	# return everything
	return t_stat, df, cv, p
def gettingInsights():
    steps_per_day,steps_per_week = csv_to_pd()
    dict4week,dict3week,dict2week = 

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