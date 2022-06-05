#!/usr/bin/env python
# coding: utf-8

# In[2]:


from Preprocessing import preprocess
import plotly.express as px
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


# In[3]:


l=preprocess()


# In[4]:


#print(l)


# In[ ]:





# In[ ]:





# In[5]:


sid = SentimentIntensityAnalyzer()
analysisp=[]
analysisn=[]
analysisnu=[]
analysisc=[]
for i in l:
    ans=sid.polarity_scores(i)
    analysisp.append(ans['pos'])
    analysisn.append(ans['neg'])
    analysisnu.append(ans['neu'])
    analysisc.append(ans['compound'])


# In[ ]:





# In[ ]:





# In[6]:


fig = px.line(y=analysisp)

fig.update_xaxes(title_text='Article Number')
fig.update_yaxes(title_text='Positive')

fig.show()
fig = px.line(y=analysisn)

fig.update_xaxes(title_text='Article Number')
fig.update_yaxes(title_text='Negative')

fig.show()
fig = px.line(y=analysisnu)

fig.update_xaxes(title_text='Article Number')
fig.update_yaxes(title_text='Neutral')

fig.show()
fig = px.line(y=analysisc)

fig.update_xaxes(title_text='Article Number')
fig.update_yaxes(title_text='Compound Value')

fig.show()


# In[7]:





# In[ ]:




