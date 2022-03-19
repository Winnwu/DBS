#!/usr/bin/env python
# coding: utf-8


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
    return(render_template("index.html", results=s))
  else:
    return(render_template("index.html", results="2"))


# In[ ]:


if __name__=="__main__":
  app.run()


# In[ ]:





# In[ ]:





# In[ ]:




