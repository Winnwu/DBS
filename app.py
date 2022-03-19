#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[5]:


df = pd.read_csv("DBS_SingDollar.csv")


# In[6]:


print(df)


# In[7]:


X = df.loc[:,["SGD"]]


# In[8]:


Y = df.loc[:,['DBS']]


# In[9]:


print(X)


# In[1]:


from sklearn import linear_model


# In[2]:


model = linear_model.LinearRegression()


# In[3]:


model.fit(X,Y)


# In[ ]:


pred = model.predict(X)


# In[4]:


from sklearn.metrics import mean_squared_error


# In[15]:


rmse = mean_squared_error(Y,pred)**0.5


# In[16]:


print(rmse)


# In[17]:


#print(rmse/Y.mean(axis=0)*100)


# In[9]:


import joblib


# In[19]:


model = joblib.load("DBS_Reg")


# In[20]:


x = [[1.5]]
pred = model.predict(x)
print(pred)


# In[5]:


from flask import Flask, request, render_template


# In[6]:


app = Flask(__name__)


# In[7]:


@app.route("/",methods=["GET","POST"])
def index():
  if request.method == "POST":
    num = request.form.get("rates")
    print(num)
    model = joblib.load("DBS_Reg")
    pred = model.predict([[(float(num))]])
    print(pred)
    s = "Predicted DBS Share Price :" + str(pred)
    print(s)
    return(render_template("index.html", results=s))
  else:
    return(render_template("index.html", results="2"))


# In[ ]:


if __name__=="__main__":
  app.run()


# In[ ]:





# In[ ]:





# In[ ]:




