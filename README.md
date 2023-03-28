# CU-Fintech_Project-2

# Installation Instructions
To clone and use:
1) make a local directory for this github repository
2) clone down this repo with git clone command
3) cd into cloned repo
4) activate conda development environment
5) install necessary dependencies via the following commands:

    pip install pandas
    pip install numpy
    pip install pathlib
    pip install -U scikit-learn
    pip install spotipy 

6) open final_compiled_notebook.ipynb Jupyter Notebook
7) run the file
8) choose song of interest in code block 40 and run blocks 40, 41, 42, 43 for a prediction if in top 50 or not

# Background of Record Labels and A&R Recruitment 

# Industry Shift to A&R Data Driven Decisions 

# Label Investment in New Talent

# Our Product: Objective, Use Scenarios, Vision, Cost to Build, Pricing Strategy

# Data & API
Spotify data was extracted from the Spotify HUGE database - daily charts over 3 years at: https://www.kaggle.com/datasets/pepepython/spotify-huge-database-daily-charts-over-3-years. We selected the US data as it was the most complete data with the majority of fields being non-null values. We used this selected data to train and test our models. We also dropped columns that were not from the original spotify API but were made by the creator of the dataset. These were mostly redundant and sometimes full of null values. Additionally, a number of columns that were supposed to be float type were stored as string type objects, and therefore had to be converted with for loop, astype algorithms. When comparing counts, we observed oversampling issues both when comparing top10 and top50 counts. This was anticipated by the team as many more songs were expected to not be a top song vs being a top song. We therefore chose to implement random oversampling methods to better match counts between these two categories in preparation for the implementation of machine learning methods and models. As the scales of various features varied significantly (ie tempo versus follower count), scaling methods were applied in order to further prep the data for the application of machine learning models. Data trimming methodes to extract inter quantile range data and exclude outliers were also experimented with for top 10 data (as seen in top-10_data-trimming-resampling-work.ipynb). The clean, scaled data were then saved as a csv and used in subsequent machine learning algorithms to develop predictive models.

# Models 

# Visualizations
A number of visualization techniques were implemented to explore various feature aspects of the data set. Visualization techniques were implemented to compare different features between top50 and non top50 categories. Using hvplot, we prepped and studied various features between these categories. Looking at artist followers, for example, we see a correlation between an increase in followers and an increase in top50 count. This served as a relative positive control suggesting our data and analysis would be potentially valid and enlightening. Interesting trends that were seen from this analysis included an increase in danceability slightly correlated with songs included in the top50 category. Conversely, an increase in length of song (duration_ms) slightly trended downward when comparing songs in the top 50 vs songs not in the top 50 ie longer songs were represented at a slightly lower frequency than shorter songs. Similarly songs with more energy seemed slightly less represented in the top50 category. A correlation matrix heatmap was also generated via hvplot suggesting some interesting trends between features of interest from the spotify data set. For example boy-band songs seem slightly negatively associated with danceability, country music is positively correlated with non-explicit music, and as potentially expected, loudness is negatively correlated with acoustics. Many interesting correlation trends can be observed from this correlation heatmap plot.


