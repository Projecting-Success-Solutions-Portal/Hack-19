# Importing the libraries
import pandas as pd
import random
from datetime import datetime, timedelta

# Data for generator
existing_data = pd.read_csv('C:\\Users\\tod83904\\Downloads\\generator.csv')
project = ['Indigo', 'Juliet', 'Kilo', 'Lima']
owner = ['Prue Halliwell', 'Leo Wyatt', 'Melinda Warner', 'Ben Cole']
bencat = ['Agriculture', 'Biodiversity', 'Disadvantaged Population', 'Disaster', 'Economy', 'Education', 'Energy', 'Environment', 'Health', 'Heritage', 'Housing', 'Local Economy', 
          'Mental Health', 'Minority Population and Inclusivity', 'Opportunities', 'Physical Health', 'Services', 'Sustainability', 'Transport']
    
# No of rows required
no_rows = 400

# Avoiding data limits
existing_data = existing_data.sample(n=max(no_rows, len(existing_data)), replace=True)

# Formatting date values and generating values
date_format = "%d/%m/%Y"
sourceProject = random.choices(project, k=no_rows)
sourceOutcome = random.choices(existing_data['Outcome'].tolist(), k=no_rows)
sourceOwner = random.choices(owner, k=no_rows)
sourceBencat = random.choices(bencat, k=no_rows)

# Producing core data
new_data = pd.DataFrame({'NewOutcome': sourceOutcome, 'NewProject': sourceProject, 'BenefitCategory': sourceBencat})

# Conditional values depending on project
new_data['Owner'] = new_data['NewProject'].apply(lambda x: owner[0] if x == 'Kilo' else
                                                       (owner[1] if x == 'Indigo' else
                                                        (owner[2] if x == 'Lima' else owner[3])))
         
new_data['ProjectStart'] = new_data['NewProject'].apply(lambda x: '26/02/2017' if x == 'Kilo' else
                                                       ('20/04/2018' if x == 'Indigo' else
                                                        ('20/07/2019' if x == 'Lima' else '15/09/2020')))

# Benefit date range depending on start date/project
def generate_random_date(project):
    if project == 'Kilo':
        start_date = datetime(2017, 2, 26)
        end_date = datetime(2019, 12, 31)
    elif project == 'Indigo':
        start_date = datetime(2018, 4, 20)
        end_date = datetime(2020, 12, 31)
    elif project == 'Lima':
        start_date = datetime(2019, 7, 20)
        end_date = datetime(2021, 12, 31)
    else:
        start_date = datetime(2020, 9, 15)
        end_date = datetime(2022, 12, 31)  
   
    random_date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
    return random_date.strftime(date_format)

new_data['BenefitStartDate'] = new_data.apply(lambda row: generate_random_date(row['NewProject']), axis=1)
new_data['BenefitStartDate'] = pd.to_datetime(new_data['BenefitStartDate'])

new_data['BenefitCompletionDate'] = new_data['BenefitStartDate'] + pd.to_timedelta([random.randint(60, 565) for i in range(no_rows)], unit='D')

date_format = "%d/%m/%Y"
new_data['BenefitStartDate']  = new_data['BenefitStartDate'].dt.strftime(date_format)
new_data['BenefitCompletionDate'] = new_data['BenefitCompletionDate'].dt.strftime(date_format)

new_data.to_csv('NewData.csv', index=False)
print(new_data)
