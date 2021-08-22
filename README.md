#  World Happiness Report
[Link to Draft Presentation in Google Slides](https://docs.google.com/presentation/d/1Mhrzv_qG6DSvkZ4WcqwE0Hmt7kNobXfSib1PZnh_w1s/edit#slide=id.ge779680b70_1_5)  

[Link to Draft Tableau Dashboard](https://public.tableau.com/app/profile/david.coyle/viz/WorldHappinessReport_16286523395800/WorldHappinessReport?publish=yes)
## Overview

The selected topic for the project is the world happiness report utilizing the world happiness dataset from Kaggle.  The central base for this data since 2013 is Sustainable Development Solutions Network and the Center for Sustainable Development at Columbia University. 

This dataset consists of numerous continuous variables presenting the opportunity to utilize multiple linear regression and random forest regression machine learning models to predict the happiness of a country or region of the world based on a set of independent variables.

The source data includes the following relevant fields for analysis.  Most countries have multiple years of data represented in the dataset.

 - Country (categorical)

 - Region of the World (categorical)

 - Year (categorical)

 - Happiness Score (continuous)

 - Economic Production (continuous)

 - Social Support (continuous)

 - Life Expectancy (continuous)

 - Freedom (continuous)

 - Absence of Corruption (continuous)

 - Generosity (continuous)



This project aimed to answer the following questions:

1)  Leveraging machine learning and the world happiness report data, can a robust, predictive model be created?

2)  What variables are most predictive of happiness score by geographical area?

3)  How has happiness changed over time by world region and country?


To accomplish the goals of this project the data set was explored and cleaned in PANDAS, a database was created using AWS/RDS and PostgreSQL in which the final data tables were created, machine learning models were constructed, and the analyses were visualized via a Tableau dashboard.

##  Database

A database was created utilizing AWS/RDS and PostgreSQL. The database houses each variable and value from both the main happiness report and 2021 happiness report csv files. By creating the world happiness report 2021 table in PostgreSQL we added 20 variables that identify social, political, psychological, and other aspects that correlate to overall happiness of a country. Many variables were removed from the final model. A table was created for the world happiness report which holds 11 variables of similar context. The two tables were combined using a UNION to create one table for the machine learning model, visualizations, and other analyses. 

## Analysis

### Exploratory Analysis

The data were investigated and cleaned primarily using PANDAS with some final parts of the process being completed in the database.  This included:

-	Adding/deleting/renaming columns

-	Addressing missing data by removing records from dataset or, when possible, filling in missing value with average score for field when country had multiple values with which to work

-	Creating a UNION of two tables in data set to have all years data in one table and have the world_region value available for every record in dataset (UNION was created in the database)

### Machine Learning Models

Two models were selected to attempt creating a robust, predictive model – Multiple Linear Regression and Random Forest. Multiple Linear Regression was selected as the starting point due to the dataset being primarily continuous data variables that directly influence the happiness score which is also a continuous variable.  Random Forest was selected as the next step in the machine learning process to see if the model could be made more robust and predictive, account for the three categorical variables through label encoding, and then rank the importance of the feature variables in the model.

There are limitations and benefits to both models: 
-	Multiple Linear Regression Model

	•	Advantages: Can be trained easily, mathematical equations are simple

	•	Disadvantages: More likely to underfit data resulting in low accuracy, outliers can heavily skew the data


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

Training and Testing Groups = X_train, X_test, y_train, y_test (Note: this test/train data set is the same as what was used for the linear regression model) 


The random forest model was expected to perform better than the multiple linear regression model and also help identify which feature variables are most important in predicting the happiness_score

To identify which variable(s) are the most predictive of a country’s happiness score, backwards elimination may be used and any independent variable with a p-value >.05 will be removed from the multiple linear regression model.  This approach will likely increase the overall R-squared score of the multiple linear regression.

Between segments 2 and 3 the team decided to remove the backwards elimination analysis and only use the variables importance ranking from the random forest model.   Additionally, the code was modified so that the same train/test data set was used in both machine learning models allowing for better performance comparison.

Given that both models were regression analyses there was no accuracy score or confusion matrix for reporting purposes.  The R-squared value was used to evaluate model performance.  The R-squared value for the multiple linear regression and random forest models were .74 and .86, respectively, indicating that the random forest model is the better model at predicting a country’s happiness score.  

Linear Regression R-squared Value

![Linear Regression R squared](https://user-images.githubusercontent.com/80165223/130359605-85ac3dfa-bb17-4c08-b313-d65629b1b8d2.png)


Random Forest R-squared Value

![Random Forest R squared](https://user-images.githubusercontent.com/80165223/130359612-130e0d2a-0ac1-4d61-8e71-9574eaeb94dd.png)


In ranking the variables of most important to least important in the random forest model, the following results were yielded, which demonstrates that economic production in the model is weighted significantly more heavily than the others:


![Random Forest Feature Importance](https://user-images.githubusercontent.com/80165223/130359592-2273435f-5adf-44d1-b56f-c79553b478ea.png)



#### Statistical Analysis

No additional statistical analyses were conducted beyond the machine learning models and the trends displayed on the Tableau dashboard.  If more time was provided, a linear regression model would be utilized to determine if there are statistically significantly changes in happiness scores over time by countries and regions.


##  Dashboard

A storyboard in Tableau (link above) was leveraged to tell the story of the data, machine learning models, and other trends observed that relate to the project goals. The final visuals focus on the predictive value of the machine learning models, the most important feature variables in predicting happiness scores, trends over time as happiness relates to world region and country, and geographical distribution of happiness.  

## Summary
The final results of the project have indicated that a random forest model is the most robust machine learning model and that economic production score is the most important variable in that model in predicting happiness.  Other feature variables that were expected to be strong predictors of happiness were significantly less predictive than economic production, like generosity and perceptions of corruption.

When evaluating trends over time regarding a country or region’s happiness score, there are fluctuations, but no trends in a single direction – happiness appears relatively stable.  Additional analyses could be conducted to see if there are statistically significant trends in happiness over time.
INSERT TIME SERIES CHART HERE FROM DASHBOARD WHEN READY

At the completion of the project the team acknowledged that additional research of the data set used for this project would have increased understanding as the background provided on Kaggle was poorly described.  Additionally, a more robust data set could be used that is related to this topic, including, including the Happy Planet Index.
