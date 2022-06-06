# Summer-2022-programming-challenge
## Contents of this repository
* Scraper python file (Scraper.py)
* Preprocessing of articles python file (Preprocessing.py)
* Sentiment Analysis and Visualization python file (sentimentandvisual.py)
* Collected unprocessed Articles titles and article text as a json file  (articles.json)
* Requirements text file
## Setup and Running of Files
Please first clone or download as .zip file of this repository.
Then extract the zip file in your directory and run the commands below in the extracted files directory on your command prompt.

```shell
cd Summer-2022-programming-challenge-main
#install virtualenv
pip3 install virtualenv
#create a virtual environment with name assign
virtualenv assign
#start the virual env
assign\Scripts\activate

#install dependencies
pip3 install -r requirements.txt

#collect articles from the website by running the scraper
python Scraper.py
#Preprocessing and Sentiment Analysis And Visualization
#Preprocessing is done when calling the sentiment and visual python file
python sentimentandvisual.py

#exit virtual env
deactivate
```
After Running the last python command the plots will be generated on the browser and thats where you can view them.
## Scraper.py
This is the code which we utilize to scrape https://www.aljazeera.com/where/mozambique/ and get its top 10 latest articles. We utilize libraries like BeautifulSoup, urllib3.request, requests, etc to help access the website and extract data from it. We first access the website using the url and then parse the website to get links from its attribute tags with class 'u-clickable-card__link'. This tag contains the links of the articles we require in its href part. After that we extract the href link associated from these articles and add them to our base link of https://www.aljazeera.com to get our exact article and its contents. We parse each of these new website links using our previous methods and get the article heading situated inside h1 tags and article texts situated inside p tags of the HTML document and dump this data into a json file.

## Articles JSON Format
 The articles in the json file are stored in a dictionary format where the headline of the article is the key and the article text is the value of that key.Both the key and value still contain some links and HTML tags present in them which will be removed in preprocessing stage.

## Preprocessing.py
This code helps to preprocess the dumped json file to make it suitable for sentiment Analysis.We import the json file as a dictionary and clean the data. Here we remove any HTML tags and the contains within those tags that are present in the headline or article text by using a regex ,this helps us to remove any images or any clickable links embedded in the HTML file added through HTML tags. Then we also use the regex to find any normal links in the articles which arent in the HTML tags and remove them . This returns us a cleaned and processed list of articles heading titles concatenated with the article data. I also used tqdm to see and visualize how long it will take to complete these tasks and see task completion percentage.

## sentimentandvisual.py
This code does sentiment analysis and visualizes its results in form of plots. I used SentimentIntensityAnalyzer from vaderSentiment to do the sentiment analysis of articles. In this file we call the preprocess function from Preprocessing.py and get the returned list and pass it through the sentiment analyzer function.This gives us the polarity of the article as a dictionary value corresponding how negative,positive,neutral and overall result(compound) it thinks the sentiment is. We store each of these individual values from the corresponding returned dictionaries into a list for plotting it. The plots are plotted using plotly library . I define the axis names and pass the corresponding lists to generate the plots.

## Plots and Results Analysis
#### Plots
![newplot](https://user-images.githubusercontent.com/59862095/172074937-a11756b0-06bf-4496-b417-8d2729307ea8.png)
Plot of Positivity sentiment of Article vs Article Number
![newplot (1)](https://user-images.githubusercontent.com/59862095/172074941-65a7b2fa-90aa-4daf-ab3c-ebb87976a7bc.png)
Plot of Negativity sentiment of Article vs Article Number
![newplot (2)](https://user-images.githubusercontent.com/59862095/172074949-9f7b804b-15ee-4a7c-997f-440f0983289b.png)
Plot of Neutral sentiment of Article vs Article Number
![newplot (3)](https://user-images.githubusercontent.com/59862095/172074952-6c25ac6c-aba2-49d7-972c-22b752a509ce.png)
Plot of Overall sentiment of Article vs Article Number

#### Results And Analysis
The overall sentiments of each Articles can be judged from the last plot which indicates if the article is Positive sentiment (with a score greater than 0) or Negative sentiment (with a score less than 0). We see articles with numbers 0,1,2,4,5,6,7,9 have a negative score which shows negative sentiments which is true for the articles as they talk about deaths and flooding and changes in government where the ministers were removed for no apparent reason or cities being captured by rebel groups which all are negative in nature. Articles 3 and 8 which have a positive sentiment are articles talking about analysis of how Africa could be the next leading producer of oil in the world and how  the troops of Mozambique recaptured a city from Rebels repectively which is good news.

From the above graphs we can also infer most of the articles have a neutral tone in majority .This maybe due to the fact of usage of more neutral words like The,This,That,It,and,etc in the article writing.The overall compound score is not greatly affected by usage of these neutral words tho they are in the majority due to the fact of english literature and how sentences are phrased. The negative and positive words dictate mostly the sentiment of these articles.

## Running Time of Code
Scraper.py - 3.67 ± 0.1977 seconds (may vary due to response time of website)

Preprocessing.py and sentimentandvisual.py - 4.00 ± 0.3956 seconds

Total time - 7.67 ± 0.5933 seconds
