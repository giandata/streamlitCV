import streamlit as st
import plotly.express as px
import plotly.figure_factory as ff
import numpy as np
import pandas as pd

st.set_page_config(page_title ="Giancarlo Di Donato",page_icon="🇮🇹")

col1, col2, col3 = st.columns([4,2,1])

with col1:
    st.title(" Giancarlo Di Donato")
    st.markdown('''#### Business Analyst''')
    st.markdown('''📧 mailto:didonatogiancarlo89@gmail.com''')
    st.markdown('''[**LinkedIn**](www.linkedin.com/in/giancarlodidonato) | [**Tableau Public**](https://public.tableau.com/app/profile/giancarlo4226) | [**Articles**](https://www.linkedin.com/in/giancarlodidonato/detail/recent-activity/posts/) | [**Source code**](https://github.com/giandata/streamlitCV)'''  )

with col2:
    st.image("pic.png")

with col3:
    st.write("")


st.write("A data driven professional, self and continuos learner. Coming from an economics background, nurtured and developed a great passion for Data Science. Technical profile with experience in organization and team management.")



st.markdown('''#### My previously developed applications:

 * [** Forecast App **](https://share.streamlit.io/giandata/forecast-app/forecastapp.py)

* [** Vaccines Tracking (Italy) **](https://share.streamlit.io/giandata/vaccini-italia-covid/dashboard.py)
''')

st.header("Professional Experiences 💼")
with st.expander("Business Analyst @Adevinta Spain"):
    st.write("June 2018 - Current")
    st.markdown(''' 
    * Gathering of requirements, data extraction, analysis, visualization and presentation for **product development, feature performance tracking, AB Testing.**
    * Data Governance and documentation: Tracking requirements, databases sources, data models for dashboards.
    * Developing in-house **coaching for analysts** on analytics tools such as Tableau and Adobe Analytics and innovation initiatives regarding data democracy and advanced analytics.
    * Participation in Data Scientists team for Machine Learning based experiments design and analysis.
    * Administration of Tableau Server Site: users and groups management, refresh troubleshooting, mail server alert system integration, testing new versions.
    * **Achievements**: Support in database migration to cloud services; helped company adopting Tableau, defined standard documentation for tracking of events and data QA ''')

with st.expander("Data & Quality Manager @HP Enterprise"):
    st.write("June 2016 - May 2018")
    st.markdown('''
    * **Coordination and monitoring of team's operations** and planning.
    * Creation of outbound campaigns for multiple teams (France,Spain,Italy,Portugal) from relation databases.
    * **Analysis and reporting automation** of team's performance to key stakeholders.
    ''')

with st.expander("Technical Advisor & Workforce monitor @WebHelp"):
    st.write("May 2015 - June 2016")
    st.markdown('''
    * **Real time monitoring of SLA and workforce planning**
    * Fraud detection and refund process
    * Technical support via inbound calls and emails
    ''')

st.header("Education 🎒")
with st.expander("Master's Degree in Business Administration & Management"):
    st.write("University of Foggia: October 2012 - March 2015")
    st.write("Final grade: **110 with Honors**")
    st.markdown('''
    Thesis in Public Economics: *"SME's internationalization as growth driver"*
    ** Statistic chapter**: *"The impact of internationalization on Firm's innovativeness: the case of Italian Manufacturing Sector".* Published in academic journals.

    **Knowledge:**
    * Mathematical models
    * Financial methods
    * Crisis management
    * Commercial and tax law
    * Business management
    * International accounting standards
     ''')
     

with st.expander("Bachelor's Degree in Economics"):
    st.write("University of Foggia: September 2008 - October 2012")
    st.markdown('''
    Thesis in technical Analysis: *"The correlation among the main financial markets".*

    ** Keywords**: Technical analysis, R, Statistical analisis, Pearson coefficient, Regression, Seasonal/Cyclic/Trend adjustments, Time Series, Dow Jones,Nikkei,Ftse 100, Ftse Mib.
    
    **Knowledge:**
    * Statistics, Mathematics
    * Business Administration
    * Private and public law
    * Financial and economics
     ''')

st.header("Courses & MOOCs 💻")

with st.expander("2021"):
    st.markdown('''
    * 2021 Python for Machine Learning & Data Science Masterclass
    * Building machine Learning Web Apps with Python
    * Getting started with AWS Machine Learning
    * Web Application from scratch with Streamlit
    ''')
with st.expander("2020"):
    st.markdown('''
    * Tableau Data Scientist
    * Tableau Designer
    * Tableau Site Administrator
    * Tableau  Developer
    * Create bespoke visualizations with Tableau
    ''')
with st.expander("2019"):
    st.markdown('''
    * Python for Data Science & Machine Learning Bootcamp, Pieran Data
    * Python Bootcamp: from 0 to hero, Pieran Data
    * NLP: Natural Language Processing with Python
    * Business Metrics for data-driven companies, Duke University
    * Data visualizaion and communiation with Tableau, Duke University 
    * Managing Big Data with MySQL, Duke University''')


st.header("Tools & Skills 🛠️")

with st.expander("Data skills"):

    df_skill = pd.DataFrame(dict(
    r=[8, 8, 10, 10, 8,9,9,8,7,8],
    theta=['Data extraction','Data preparation','Data analysis','Data visualization','Web Applications',
        'Web data tagging','Digital Analytics','Data Governance','Machine Learning','Forecasting']))

    fig = px.line_polar(df_skill, r='r', theta='theta', line_close=True)
    fig.update_traces(fill='toself')
    st.plotly_chart(fig,use_container_width=True)

with st.expander("Softwares & Languages"):
    df_tool = pd.DataFrame(dict(
    r=[8, 10, 8, 9, 7,8,9,7,8],
    theta2=['SQL','Tableau','Streamlit','Adobe Analytics','Python','Jupyter','Excel','Machine Learning','Prophet']))
    
    fig = px.line_polar(df_tool, r='r', theta='theta2', line_close=True)
    fig.update_traces(fill='toself')
    st.plotly_chart(fig,use_container_width=True)

with st.expander("Soft Skills"):
    df_soft = pd.DataFrame(dict(
    r=[9, 9, 7, 8, 9,8,8,8],
    theta2=['Communication','Presentation','Market Research','Agile Methodology','Planning & organization','Critical Thinking','Team Management','Project Management']))
    
    fig = px.line_polar(df_soft, r='r', theta='theta2', line_close=True)
    fig.update_traces(fill='toself')
    st.plotly_chart(fig,use_container_width=True)

st.header("Personal Development 🌱")

with st.expander("Languages"):
    st.markdown('''
    * Native Italian
    * Proficient English
    * Proficient Spanish''')

with st.expander('Hobbies'):
    st.markdown('''
    * Chess, beer crafting
    * Rock music or Melodic Techno 
    * Football and archery
    * Ancient History ''')