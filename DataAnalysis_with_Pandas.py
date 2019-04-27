#!/usr/bin/env python
# coding: utf-8

# In[26]:


import pandas as ps


# In[27]:


employee = ps.read_table("C:/MyDocuments/ProfessionalDevelopment/TechnicalSkillDevelopment/DataScience/UdemyCourses/LearnDataAnalysisWithPandas/Resources/Tab_separated_values.tsv")
employee.head()

cols = ["Name", "Position"]
employee[cols]


# In[28]:


employee.dtypes


# In[29]:


import numpy as np
employee = ps.read_table("C:/MyDocuments/ProfessionalDevelopment/TechnicalSkillDevelopment/DataScience/UdemyCourses/LearnDataAnalysisWithPandas/Resources/Tab_separated_values.tsv")
#employee.select_dtypes(include=[np.number]).dtypes


# In[11]:


employee.describe()


# In[15]:


#find out number of columns and rows
employee.shape


# In[30]:


employee["Name Salary"] = employee["Name"]+employee["Salary"]
employee.head()


# In[33]:


employee.drop(['Age'], axis=1, inplace=True)
employee.head()


# In[35]:


employee = ps.read_table("C:/MyDocuments/ProfessionalDevelopment/TechnicalSkillDevelopment/DataScience/UdemyCourses/LearnDataAnalysisWithPandas/Resources/Tab_separated_values.tsv")
employee.head()
cols = ["Name", "Pos", "Ofc", "Age", "S_date", "Sal"]
employee.columns = cols
employee.head()


# In[36]:


employee.sort_values(by="Age", ascending=True)


# In[39]:


employee["Name"].sort_values().head()


# In[42]:


b


# In[43]:


employee[(employee.Age < 30 ) & (employee.Ofc == "London")]


# In[44]:


#filter columns
cols = ["Name", "Pos"]
employee[(employee.Age<40) & (employee.Ofc=="London")][cols]


# In[46]:


#chapter 6 - •	Filtering 
employee[(employee.Name!="Airi Satou") & (employee.Name!="Angelica Ramos") & (employee.Name!="Bradley Greer")]


# In[47]:


#chapter 6 - mean()
employee.mean()


# In[49]:


#Chapter 6 - •	String manipulation techniques (upper, lower, replace)
employee.Name.str.upper().head()


# In[52]:


employee.Pos.str.contains("Software").head()


# In[57]:


employee[employee.Pos.str.contains("Software")].head()


# In[55]:


#Chapter 6- o	String replace
employee.Pos.str.replace("Engineer", "Developer").head()


# In[59]:


#chapter 6 - Aggregations
employee.Age.min()
employee.Age.max()


# In[61]:


#chapter 6 - •	Groupby clauses (like you use in SQL Aggregations)
employee.groupby("Pos").Age.min().head()


# In[64]:


#chapter 6 - •	Groupby clauses (like you use in SQL Aggregations)
employee.groupby("Pos").Age.agg(['count', 'min', 'max']).head()


# In[68]:


#chapter homework - calculate the mean rowwise and columnwise
import numpy as np
iris = ps.read_table("C:/MyDocuments/ProfessionalDevelopment/TechnicalSkillDevelopment/DataScience/UdemyCourses/LearnDataAnalysisWithPandas/Resources/Iris.csv", sep=",")


# In[66]:


iris.head()


# In[69]:


iris.mean()


# In[72]:


#add a new column to store mean that's calculated by rows
iris["mean"]=iris.mean(axis=1)
iris.head()


# In[73]:


#calculate mean by columns
iris.mean(axis=0)


# In[75]:


#chapter 7 - loc : select rows and columns, like table slicing
iris.loc[0, :]


# In[76]:


iris.loc[0:3, :]


# In[81]:


iris.loc[0:3, ["sepal length", "petal width", "iris"]]


# In[83]:


iris.loc[iris.iris=="Iris-setosa"]


# In[87]:


employee = ps.read_table("C:/MyDocuments/ProfessionalDevelopment/TechnicalSkillDevelopment/DataScience/UdemyCourses/LearnDataAnalysisWithPandas/Resources/Tab_separated_values_missingvalues.tsv")
employee.head()
employee.shape


# In[89]:


#drop rows with any empty value
employee.dropna(how="any").shape


# In[91]:


employee.fillna(value=0).head()


# In[93]:


#chapter 8 - work with plot
iris = ps.read_csv("C:/MyDocuments/ProfessionalDevelopment/TechnicalSkillDevelopment/DataScience/UdemyCourses/LearnDataAnalysisWithPandas/Resources/Iris.csv", sep=",")
iris.head()
iris.shape


# In[97]:


iris.head()


# In[100]:


cols=["sepal length", "iris"]
iris[cols].plot()


# In[103]:


#join tables
dataframe1 = ps.DataFrame({"employee":["ABC", "XYZ", "MNO"], "age":[22, 35, 43]})
dataframe1


# In[105]:


dataframe2 = ps.DataFrame({"employee":["ABC", "XYZ", "EFG"], "salary":[10000, 30000, 25000]})
dataframe2


# In[107]:


#inner join
dataframe3 = ps.merge(dataframe1, dataframe2, on="employee")
dataframe3


# In[108]:


#outer join
dataframe4 = ps.merge(dataframe1, dataframe2, how="outer")
dataframe4


# In[109]:


dataframe3 = ps.merge(dataframe1, dataframe2, how="left")
dataframe3


# In[110]:


dataframe3 = ps.merge(dataframe1, dataframe2, how="right")
dataframe3


# In[114]:


#chapter 9 - pivot data
webhits = ps.read_csv("C:/MyDocuments/ProfessionalDevelopment/TechnicalSkillDevelopment/DataScience/UdemyCourses/LearnDataAnalysisWithPandas/Resources/webhits.csv")
webhits


# In[115]:


#pivode data
webhits.pivot(index="Page_Name", columns="Date")


# In[116]:


##pivot table
webhits.pivot_table(index="Page_Name", aggfunc="sum")


# In[117]:


webhits.pivot_table(index="Page_Name", aggfunc="mean")


# In[120]:


webhits.pivot_table(index="Page_Name", aggfunc="count")


# In[121]:


webhits


# In[122]:


webhits.shift(1)


# In[123]:


webhits.shift(-1)


# In[125]:


webhits.shift(-1).to_csv("C:/MyDocuments/ProfessionalDevelopment/TechnicalSkillDevelopment/DataScience/UdemyCourses/LearnDataAnalysisWithPandas/Resources/webhits_shiftup.csv")


# In[126]:


webhits.shift(2).to_csv("C:/MyDocuments/ProfessionalDevelopment/TechnicalSkillDevelopment/DataScience/UdemyCourses/LearnDataAnalysisWithPandas/Resources/webhits_shift_somecolumns.csv", columns=["Date", "Page_Name"])


# In[129]:


#use shift to calculate delta
webhits["Prev_hits"]=webhits["Hits"].shift(1)
webhits


# In[130]:


webhits["Hits_delta"] = webhits["Hits"]-webhits["Prev_hits"]
webhits

