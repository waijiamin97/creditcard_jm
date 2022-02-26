#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask


# In[2]:


app = Flask(__name__)


# In[3]:


from flask import request, render_template
import joblib

@app.route("/", methods=["GET","POST"])
def index():
    if request.method == "POST":  
        purchases = request.form.get("purchases")
        suppcard = request.form.get("suppcard")
        purchases = float(purchases)
        suppcard = float(suppcard)
        print(purchases,suppcard)
        
        model1 = joblib.load("CCU DT")
        pred1 = model.predict([[purchases,suppcard]])
        s1 = "The score of credit card upgrade based on Decision Tree Model is :" +str(pred1)
        
        model2 = joblib.load("CCU GB")
        pred1 = model.predict([[purchases,suppcard]])
        s2 = "The score of credit card upgrade based on Gradient Boosting Model is :" +str(pred2)
        
        model3 = joblib.load("CCU NN")
        pred3 = model.predict([[purchases,suppcard]])
        s3 = "The score of credit card upgrade based on Neural Network Model is :" +str(pred3)
        
        model4 = joblib.load("CCU RF")
        pred4 = model.predict([[purchases,suppcard]])
        s4 = "The score of credit card upgrade based on Random Forest Model is :" +str(pred4)
        
        model5 = joblib.load("CCU Reg")
        pred5 = model.predict([[purchases,suppcard]])
        s5 = "The score of credit card upgrade based on Logistics Regression Model is :" +str(pred5)
        
        
        return(render_template("index.html",result1= s1, result2=s2, result3=s3, result4=s4, result5=s5))
    else:
        return(render_template("index.html",result1="2", result2="2", result3="2", result4="2", result5="2"))


# In[ ]:


if __name__=="__main__":
    app.run()


# In[ ]:




