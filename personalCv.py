import streamlit as st

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

st.title(" Giancarlo Di Donato")

path = "pic.png"
image = Image.open(path)
st.image(path)

st.write("A data driven professional, self and continuos learner. Coming from an economics background, nurtured and developed a great passion for Data Science. Technical profile with experience in organization and team management.")

st.header('''My previously developed applications:

[Forecast App]([https://share.streamlit.io/giandata/forecast-app/forecastapp.py)

[Vaccines Tracking (Italy)](https://share.streamlit.io/giandata/vaccini-italia-covid/dashboard.py)
''')

st.header("Professional Experiences 💼")
with st.expander("Business Analyst @Adevinta Spain"):
    st.write("June 2018 - Current")
    st.markdown(''' 
    * Organized and prioritized work to complete projects in a timely, efficient manner. **Team player**
    * Gathering of requirements, data extraction, analysis, visualization and presentation for **product development, feature performance tracking, AB Testing.**
    * Data Governance and documentation of data projects.
    * Developing in-house **coaching for analysts** on analytics tools and innovation initiatives regarding data democracy and advanced analytics.
    * **Administration of Tableau Server Site**: users and groups management, refresh troubleshooting, mail server alert system integration, testing new versions.''')

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
    st.write("Final grade: **110 with Honors**")
    st.markdown('''
    Thesis in technical Analysis: *"The correlation among the main financial markets".*

    ** Keywords**: Technical analysis, R, Statistical analisis, Pearson coefficient,Regression,Seasonal/Cyclic/Trend, Time Series, adjustmentsDow Jones,Nikkei,Ftse 100, Ftse Mib.
    
    **Knowledge:**
    * Statistics, Mathematics
    * Business Administration
    * Private and public law
    * Financial and economics
     ''')

st.header("Courses & MOOCs")

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
