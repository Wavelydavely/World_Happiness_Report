#  Predicting World Happiness

## Overview
The selected topic for the project is predicting world happiness utilizing the world happiness dataset from Kaggle. This dataset consists of numerous continuous variables presenting the opportunity to utilize a multiple regression machine learning model to predict the happiness of a country or region of the world.  Additionally, using backwards elimination, the variables that are the least predictive of the happiness score can be removed to improve the performance of the model.

The source data includes the following relevant fields for analysis:
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

Most, if not all, countries have multiple years of data represented in the dataset.

In this project, we are aiming to answer the following questions:
What variables are most predictive of happiness by country?
What variables are most predictive of happiness by region of the world?
Which region’s happiness has gone up the most throughout the years? Which have gone down?


## GitHub
Each member of the team has a branch in the World_Happiness_Report repository where code will be committed before merging with the main branch.  Any code being merged to the main branch will be reviewed to avoid conflicts during the process.

## Communications
Communication within the team will also occur outside of GitHub via slack, Google Docs, and video to ensure proper use of GitHub.  Team roles will be defined at the start of each week to avoid duplication of work and thus increasing the chances of merge conflicts.
 
## Machine Learning Model
Given that the data set includes majority continuous variables that would be used for predictive modeling, a multiple linear regression machine learning model was chosen. To access this data, the machine learning model will connect to our provisional database, likely in PostgreSQL.
There are 6 independent variables that will be utilized in the model – economic production, social support, life expectancy, freedom, absence of corruption, and generosity – to predict the dependent variable – happiness score.  All of these variables will be used to train the model.
The R-squared score, as an output of the model, will help determine the strength of the initial multiple linear regression model and whether it is predictive of the happiness score.  A score higher than .75 will be ideal; however, a lower score may be accepted as some of the variables measure human perception, which adds complexity to the model.
To identify which variable(s) are the most predictive of a country’s happiness score, backwards elimination will be used and any independent variable with a p-value >.05 will be removed from the multiple linear regression model.  This approach will likely increase the overall R-squared score of the multiple linear regression.
 
##  Database
A provisional database, likely in PostgreSQL, will be created and referenced in the machine learning model overview. The database will house each variable and value from both the main happiness report and 2021 happiness report csv files.
By creating the world happiness report 2021 table in pgAdmin we are going to add 20 variables that identify social, political, psychological, and other aspects that correlate to overall happiness of a country. Some of these variables will likely be removed from the final model. A table will also be created for the world happiness report which holds 11 variables of similar context. The two tables will then be joined to create one table for the machine learning model, visualizations, and other analyses. To do this we will need to rename, match, and add columns via python pandas so we can successfully join in SQL. 
