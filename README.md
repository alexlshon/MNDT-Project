# Mapping Situation Awareness: 
## Identifying Earthquake Related Tweets
![Imgur](https://i.imgur.com/yFiVxvZ.png)
### *Project Contributors: Alex Shon, Andy Zhang, Charles Spalding, Raymond Paller*
_______________________

### Introduction
Shortly after a major natural disaster, responding to people in affected areas needs to be swift. Whether it is staying informed, sending out updates about the affected area, or a cry for help; social media has played an increasing role in disaster response. We are all aware of the role that social media can play on a Natural disaster. Twitter is mentioned in the news on reports of global supports and response campaigns. Crowdsourcing efforts for repairs and support can reach their goal two times over. And local volunteers can organize and mobilize in response to ever changing crises. Civilians in hurricane Sandy (2012) sent more than *20 million tweets* related to the storm both during and shortly after. Using social media posts is crucial for effective disaster response. 

Response efforts are better organized and planned when reading a map of the affected area displaying the magnitude of impact. Globally, 71 countries and territories are developing disaster reduction strategies aligned with the United Nations.  The U.N continues to provide technical guidance, for example, by establishing disaster loss databases used by affected nations. The United States establishes agencies which monitor natural disaster events and respond to moments of crisis. Earthquakes are reported by the United States Geological Survey (USGS). In effort to map real time reporting via social media of natural disaster affected areas, we reach to our problem statement: **Can social media posts be mapped to show the spread of situational awareness of an earthquake?**
______________________
### Data Collection
Our team worked to produce a training dataset and a testing dataset. The Training data set came from the research of [Muhammed et al. (2016)](https://crisisnlp.qcri.org/#)\*. The training set contained almost 12,000+ tweets relevant to 4 major earthquakes  There are a multitude of social media platforms available to monitor in the wake of a natural disaster. For our main source of social media to use as our testing data, we decided to use Twitter for several reasons: 
1. Because it the most immediate and real time social media
2. Easy set up of the twitter API allowed us to maximize our efforts in the project timeline
3. The API allowed for area searching with tweets tagging their exact location.

After deciding using twitter, In order to create several training datasets, manually labeling the tweets was required. A testing set of 600+ earthquake relevant tweets were collected. A major challenge for the overall project is only 3% of Twitter is searchable by their geo location. Which makes the data collection more biased. However, most earthquakes go unrepresented in the media, and no major earthquakes occurred during the project production. So tweets that were tagging their location and labeled relevant were mainly from government sponsored reporting agencies.
__________________________________________________
### Preprocessing & Modeling
Both the training and testing sets were cleaned and transformed with the same pipeline order:

*Cleaning:*
- NLTK RegeTokenizer was used to separate the words 
- Special characters were then striped away
- All words were then set to lowercase

From the timeframe given, replacing acronyms and commonly used shorthand of twitter was not applied to the data. Many features may have been repetitive in their context. 

The tweets were then transformed in a TFiDFVectorizer (tvec) from the sklearn framework. The tvec was tuned using a GridSearch method measuring on accuracy of a logistic regression. English stopwords were used with a 5,000 limit of features out of a (1, 2) ngram range. Once transformed, 8 classification techniques were tested to find the highest accuracy score. Their training and testing scores are listed in the table below:

![Imgur](https://i.imgur.com/BQtukgM.png)

The Random Forest was identified as the best performing for highest  score on testing and smallest difference between the training and testing score. Predictions made from the random forest were then sent to a SQLite database to connect with the web application.
_____________________________________________________________
### Application Development

![Imgur](https://i.imgur.com/k0L1GZx.png)

For a practical application of our results, a web app is created that implements an interactive map in a web browser.	Before a tweets are mapped,  The backendend must call on the data processing, modeling, and necessary databases. The architecture of the back-end has three components, the database, the web app framework and the data processing code. The data processing code is the jupyter notebooks used in the data analysis ported into python files for easy api access. The database is built using the SQLite package. Once tweets are classified as relevant to the natural disaster, the tweet data is stored in the database to be accessed by the web app. The flask framework generates html pages from templates and handles the get and post requests. Flask pulls the tweet data from the database and generates an html file containing the data in GeoJSON format. The interactive map is generated using javascript and css from the Leaflet package. Leaflet reads in the GeoJSON to map the tweets in an easy to use web application.   The markers of the tweets are placed on the map using longitude and latitude data. When the user clicks on to produce, a pop up which expands and shows the body of the tweet. The Leaflet package generates an interactive map using pre-installed javascript and css. Using Leaflet, our map gives the user full interactivity in changing the zoom and the area mapped. 
____________________________________________________________
### Conclusion  
This project lead our team to three main takeaways, next steps, and recommendations:
##### Takeaways
*First*, our testing data was collected from the USGS. We were able to narrow our search to affected area to confirm that the model was able to identify new tweets as relevant or not relevant. Thankfully we did not have any major natural disaster to test our model on, but its performance appears to be incredibly high for what we collected. 

*Second*, In the 2016 paper by Muhammad et al., they split their classes to identify into 7 different categories, all of course with high overlapping verbiage. When reducing the amount of categories, all models performed with a 20 point increase compared to our fellow researchers findings. Should it be the desire of a company to map urgent messages, we recommend a narrow focus on such concepts. Categorizing tweets as “Sending Condolences” or “Helpful advice” will not contribute to the actual goal as focusing on message expressing a life or death situation. 

*Third*, to successfully map situational awareness from social media; it is dependent on the users of the platform to openly share their location information. With growing concerns for privacy, we expect a large portion of the population to be left out of the analysis. 
##### Next Steps 
 - A multiclass Classification model is appropriate, but limiting the division of classes need to be considered for the model’s ability. Identifying a posts as urgent and not urgent would be a perfect step forward to developing a deployable product.
 
 - The latency needs to be reduced for the sake of competing with other agencies. While we have a map that is mapping tweets to the area of an earthquake, it only updates every 2.5 days, and therefore, we’re already 2.5 days behind the entire Internet.
 
 - Filtering misinformation is a direction and consideration that needs to be addressed for those trying to help and respond to a crisis. Misinformation is official recognized by the homeland security office and they have released a white paper detailing all of the way misinformation distorts crisis relief efforts
 
##### Recommendations
- The popularity of social media giants like Facebook and Twitter is not guaranteed and any project using social media should be aware of the platforms and their popularity amongst the different nations and social groups. While the online landscapes change in popularity, the platforms themselves are ever-evolving.

- With the competition to provide the most in demand services, platforms and users are turning to non-text based services as their preferred medium of communication. Applications such as Snapchat have emphasized the desire to share video “stories”, so much so that even facebook and instagram are deploying the option to post videos to a user’s stories or wall for their followers to follow.

- And finally, something that is easily implementable today, would be simply be having a crisis push notification. Whether it actually be initialized during an event,  or simply a check box for people to turn on and off for sending their location in an emergency. Even though it is not the responsibility of a social media platform to save lives. They can do their part so that we can do ours.

____________________________________________________________
### Sources
- [Python-twitter API documentation](https://python-twitter.readthedocs.io/en/latest/twitter.html)
- [USGS data](https://earthquake.usgs.gov/) 
   - [Direct CSV download](https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.csv.)
- [Flask tutorial](https://flask.palletsprojects.com/en/1.1.x/tutorial/)
- [CrisisNLP website](https://crisisnlp.qcri.org/#)
- [Pew reasearch Center: Twitter served as a lifeline of information during Hurricane Sandy](https://www.pewresearch.org/fact-tank/2013/10/28/twitter-served-as-a-lifeline-of-information-during-hurricane-sandy/)

\* Muhammad Imran, Prasenjit Mitra, and Carlos Castillo: Twitter as a Lifeline: Human-annotated Twitter Corpora for NLP of Crisis-related Messages. In Proceedings of the 10th Language Resources and Evaluation Conference (LREC), pp. 1638-1643. May 2016, Portorož, Slovenia.
