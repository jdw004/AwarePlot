#suicides wealthy vs poor
All_Suicides = df['Suicides number'].values.astype(float)
All_GDP = df['GDP'].values.astype(float)
#PER CAPITA ALREADY
All_Year = df['Year'].values.astype(float)
All_Population = df['Population'].values.astype(float)
All_School = df['Schooling'].values.astype(float)




Yearly_Poor_Suicides =  [0 for j in range(16)]
Yearly_Poor_Suicides_Count =  [0 for j in range(16)]


Each_Year = [2000 + i for i in range(16)]


Yearly_Wealthy_Suicides = [0 for j in range(16)]
Yearly_Wealthy_Suicides_Count = [0 for j in range(16)]


Yearly_Schooling = [0 for j in range(16)]
Yearly_Schooling_Count = [0 for j in range(16)]


i = 0
for i in range(len(df)):
  index =  int(All_Year[i] - 2000)
  Yearly_Schooling[index]+=All_School[i]
  Yearly_Schooling_Count[index] +=1


  if All_GDP[i] > 10000:
   Yearly_Wealthy_Suicides[index]+=All_Suicides[i]
   Yearly_Wealthy_Suicides_Count[index]+=All_Population[i]
   Yearly_Schooling[index]+=All_School[i]
   Yearly_Schooling_Count[index] +=1


  else:


    Yearly_Poor_Suicides[index]+=All_Suicides[i]
    Yearly_Poor_Suicides_Count[index]+=All_Population[i]




Yearly_Poor_Suicide_Rate = [100*Yearly_Poor_Suicides[i]/Yearly_Poor_Suicides_Count[i] for i in range(16)]
Yearly_Wealthy_Suicide_Rate = [100*Yearly_Wealthy_Suicides[i]/Yearly_Wealthy_Suicides_Count[i] for i in range(16)]
Yearly_AVG_Schooling = [Yearly_Schooling[i]/Yearly_Schooling_Count[i] for i in range(16)]
fig, ax = plt.subplots(1, 1)




# Calculate the linear regression trendline
slope, intercept, r_value, p_value, std_err = linregress(Each_Year, Yearly_Poor_Suicide_Rate)
trendline = intercept + slope * All_Year



slope2, intercept2, r_value, p_value, std_err = linregress(Each_Year, Yearly_Wealthy_Suicide_Rate)
trendline2 = intercept2 + slope2 * All_Year


ax.plot(All_Year, trendline, color='red', linestyle='dashed')
ax.plot(All_Year, trendline2, color='blue', linestyle='dashed')




ax.scatter(Each_Year,Yearly_Poor_Suicide_Rate, color = 'red',label ='Poor Suicide Rate' )
ax.scatter(Each_Year,Yearly_Wealthy_Suicide_Rate,color = 'blue',label= 'Wealthy Suicide Rate(GDP>10,000)')
ax.set_xlabel('Year')
ax.set_ylabel('Suicide Rate(%)')
plt.title('Suicide Rates')
plt.legend()
plt.show()
