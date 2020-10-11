# Python-NU-Lab-2
**Python Lab #2 Task**

*Questions*

<p>1:   In this lab, we will focus on taking input from different sources. Data may be incomplete and there may be missing values. The objective is to combine data and save it as one 
dataframe object. Do the following steps
</p>
<ul>
<li><p>Read data1.csv and data2.csv as df1 and df2 dataFrames objects respectively. Use Pandas I/O libraries. Use column 0 as index for df1 and column 1 as index for df2. Print df1 and df2</p></li>
<li><p>Modify (a) to concatenate df1 and df2 and assign it to df3. Print df3</p></li>
<li><p>Read data3.csv as df4 dataframe object and print df4 (not shown below). There are 2 new column ‘D’ and ‘E’ in this file. Merge df4 with df3 so that new dataframe (df5) has total 5 columns (A, B, C, D, E)</p></li>
<li><p>Read data.json as df6 and concatenate with  df5. Use df7 as name of dataframe</p></li>
<li><p>Replace Hello with NaN. Make it as general as possible so that all strings in dataframe df7 automatically becomes NaN</p></li>
<li><p>Replace NaN with mean values of the columns. Save the final dataframe as “newdata.csv”</p></li>
</ul>
<p>
<p>
** Complete the following program**<br />
import pandas as pd<br />
data = {'cities' : ['lahore','karachi',], 'provinces' : ['punjab','sindh']}<br />
<br />
*store data as DataFrame object. Assign object name as frame1*<br />
frame1 = _pd.DataFrame(data)____<br />
<br />
*print frame*<br />
....print(frame1)....<br />

data2 = {"cities": ["islamabad","karachi","peshawar","quetta"],
  "provinces": ["capital","sindh", "KPK","Balochistan"]}<br />

*store data as DataFrame object. Assign object name as frame2*<br />
frame2 = ....pd.DataFrame(data2)....<br />

*combine both objects frame1 and frame2; without any duplicate rows and re-arrange all indexes*<br />
frame3 = ....pd.concat([frame1,frame2])....# combine frame1 and frame2<br />
frame3 = ....frame3.drop_duplicates().... # remove duplicates rows<br />
frame3 = ....frame3.sort_values(by='provinces' , inplace=True)....# sort based on provinces<br />
frame3 = ....frame3.reindex(range(2), method='ffill')....# re-arrange all indexes<br />
....print(frame3)....# print frame3<br />
</p>
