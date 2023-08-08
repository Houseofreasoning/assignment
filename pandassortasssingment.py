import pandas as pd
import openpyxl as excel
myfile=pd.read_excel(r"C:\Users\USER\Videos\data\olympics.xlsx",skiprows=4)
df=pd.DataFrame(myfile)
print(df)
print(df.head())
#Top 3 countries
Years=df[(df['Edition']>=1984) & (df['Edition']<=2008)]
t_c=Years['NOC'].value_counts().head(3)
print('\033[1mTop 3 countries that have won the most medals in recent years from '
      '1984 to 2008 are listed below\033[0m:\n',t_c)
print()

male_gold_medal_winners=df[(df['Edition']>=1984) & (df['Edition']<=2008) &
                         (df['Event']=='100m') & (df['Medal']=='Gold') & (df['Event_gender']=='M')]
male_gold_medal_winners_sort=male_gold_medal_winners.sort_values(by='Edition', ascending=False)
Final_result=male_gold_medal_winners_sort[['City','Edition','Athlete','NOC']]
print('\033[1mMALE GOLD MEDAL WINNERS FOR 100m SPRINT \033[0m')
print(Final_result)