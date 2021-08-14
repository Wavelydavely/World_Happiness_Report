#  World Happiness Report
Link to Draft Presentation in Google Slides  

## Overview

The selected topic for the project is the world happiness report utilizing the world happiness dataset from Kaggle.  The central base for this data since 2013 is Sustainable Development Solutions Network and the Center for Sustainable Development at Columbia University. 

This dataset consists of numerous continuous variables presenting the opportunity to utilize multiple linear regression and random forest regression machine learning models to predict the happiness of a country or region of the world based on a set of independent variables.

The source data includes the following relevant fields for analysis.  Most countries have multiple years of data represented in the dataset.

Country (categorical)

Region of the World (categorical)

Year (categorical)

Happiness Score (continuous)

Economic Production (continuous)

Social Support (continuous)

Life Expectancy (continuous)

Freedom (continuous)

Absence of Corruption (continuous)

Generosity (continuous)


This project aimed to answer the following questions:

Leveraging machine learning and the world happiness report data, can a robust, predictive model be created?

What variables are most predictive of happiness score by geographical area?

How has happiness changed over time by world region and country?

To accomplish the goals of this project the data set was explored and cleaned in PANDAS, a database was created using AWS/RDS and PostgreSQL in which the final data tables were created, machine learning models were constructed, and the analyses were visualized via a Tableau dashboard.

## Project Team Communications

Each member of the team created branches specific to tasks in the World_Happiness_Report repository where code was committed before merging with the main branch.  Any code being merged to the main branch was reviewed to avoid conflicts during the process. Communication within the team also occurred outside of GitHub via slack, Google Docs, and Zoom to ensure proper use of GitHub.  

Team roles were defined at the start of each week to avoid duplication of work and, therefore, increasing the chances of GitHub merge conflicts.  Status updates of each team member’s tasks for the week were provided at the start of each meeting.  The group addressed issues with the project and in GitHub in team meetings and with student support. 

## Analysis

### Exploratory Analysis

The data were investigated and cleaned primarily using PANDAS with some final parts of the process being completed in the database.  This included:

-	Adding/deleting/renaming columns

-	Addressing missing data by removing records from dataset or, when possible, filling in missing value with average score for field when country had multiple values with which to work

-	Creating a UNION of two tables in data set to have all years data in one table and have the world_region value available for every record in dataset

### Machine Learning Models

Two models were selected to attempt creating a robust, predictive model – Multiple Linear Regression and Random Forest. Multiple Linear Regression was selected as the starting point due to the dataset being primarily continuous data variables that directly influence the happiness score which is also continuous.  Random Forest was selected as the next step in the machine learning process to see if the model could be made more robust and predictive, account for the three categorical variables through label encoding, and then rank the importance of the feature variables in the model.

There are limitations and benefits to both models: 
-	Multiple Linear Regression Model

•	Advantages: Can be trained easily, mathematical equations are simple

•	Disadvantages: More likely to underfit data resulting in low accuracy, outliers can heavily skew the data, overly


-	Random Forest Model

•	Advantages: Robust against overfitting, improves accuracy, ranks importance of variables, and works well with thousands of categorical and continuous variables

•	Disadvantages: High number of trees uses a lot of memory, does not determine significance of each variable


#### Multiple Linear Regression 

For the multiple linear regression model the data was split into target and feature variables groups and then into training and testing data sets.  Variables were also scaled using Standard.Scaler()

Target Variable  = happiness_score
Feature Variables = economic_production, social_support, life_expectancy, freedom, generosity, and perception_of_corruption
Training and Testing Groups = X_train, X_test, y_train, y_test

The R-squared score, as an output of the model, will help determine the strength of the initial multiple linear regression model and whether it is predictive of the happiness score.  A score higher than .75 will be ideal; however, a lower score may be accepted as some of the variables measure human perception, which adds complexity to the model.

#### Random Forest Model

For the random forest model the categorical variables were encoded as numeric values using the LabelEncoder(), the data was split into target and feature variables groups and then into training and testing data sets.  Variables were also scaled using Standard.Scaler()

Target Variable  = happiness_score
Feature Variables = economic_production, social_support, life_expectancy, freedom, generosity, perception_of_corruption, country, year, and world_region
Training and Testing Groups = X_train, X_test, y_train, y_test

The random forest model was expected to perform better than the multiple linear regression model and also help identify which feature variables are most important in predicting the happiness_score

To identify which variable(s) are the most predictive of a country’s happiness score, backwards elimination may be used and any independent variable with a p-value >.05 will be removed from the multiple linear regression model.  This approach will likely increase the overall R-squared score of the multiple linear regression.
 

##  Database

A database was created utilizing AWS/RDS and PostgreSQL. The database houses each variable and value from both the main happiness report and 2021 happiness report csv files. By creating the world happiness report 2021 table in PostgreSQL we added 20 variables that identify social, political, psychological, and other aspects that correlate to overall happiness of a country. Many variables were removed from the final model. A table was created for the world happiness report which holds 11 variables of similar context. The two tables were combined using a UNION to create one table for the machine learning model, visualizations, and other analyses. 

##  Dashboard
A storyboard in Tableau was leveraged to tell the story of the data, machine learning models, and other trends observed that relate to the project goals. The final visuals will focus on the predictive value of the machine learning models, the most important feature variables in predicting happiness scores, trends over time as happiness relates to world region and country, and geographical distribution of happiness.  Interactive features will be applied including slicers to focus on time period, country, or world region.  Additional drill down features will also be implemented to dig deeper into individual feature scores that determine the countries’ happiness scores.
