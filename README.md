# clustering-hate-speech-reddit
## Understanding Hate Speech on Reddit Comments

Hate speech is, speech designed to promote hatred on the basis of race, religion, sexual preference, ethnicity or national origin. Most of the research dealing with hate and hate speech has examined the practices and discourses of hate groups and hate crimes. This work has tended to focus on hate and hate speech on internet through Reddit website comments. The Internet has had a revolutionizing influence on groups that use of hate speech and it has played important roles in the recruitment of people into the hate movement and promoted violence against other people.
Reddit is a social platform where users submit posts that other users can reply and vote for it. Reddit is split out into sub-communities, or subreddits. They can be created by any user around any subject. Although a lot of people is using this platform, they don’t have to supply information much more than email and a username. This anonymity may result higher hate speech comments on this platform. Worked over … Reddit comments from 2017 and only selected subreddits & keywords. The first thing that had been done is generating hate speech keyword list that aims to capture comments about racism, misogynistic and homophobic views. Text clustering techniques had been implemented on generated dataset and the results had been visualized, therefore insights had been acquired through text clusters. This project aims to understand hate speech topics through perspective of big data methods. In this project, 30 cluster had been prepared with 30 most important words in it.

I had used Reddit’s comments dataset, which is an enourmous public dataset contains all publicly available comments, submissions and their information from Reddit website. The timeline of the dataset is 2005 to 2018 and it is nearly 1.7 billion comments & 250 GB as compressed [20]. Both comments and submissions are available as a compressed JSON file but only comments had been used in this analyze. Whole dataset is available on https://files.pushshift.io/reddit/comments/ website in the breakdown of months and also available on Google Bigquery platform. BigQuery is a RESTfulweb service that enables interactive analysis of massively large datasets working in conjunction with Google Storage. It is an Infrastructure as a Service(IaaS) that may be used complementarily with MapReduce. BigQuery was designed for analyzing data on the order of billions of rows, using a SQL-like syntax.

Below table shows the total number of comments in the whole dataset, this number acquired through a simple SQL query from BigQuery platform.


**Number of Comments: 4,110,048,925**

Below table shows the total number of unique subreddits in the whole dataset, this number also acquired through a simple SQL query from BigQuery platform.

**Number of Unique Subreddits 633,033**

eddit dataset is one of the biggest text dataset among the publicly available datasets, therefore only a slice of the dataset had been used in this project. I chose 2017 for data analyzing. Below table shows the sizes of processed dataset, initial downloaded file was compressed “.bz” file, through Unix bash code, it had been unzipped as a JSON file. Further filtering was done via “JQ” tool.

Month    Filtered_Json	Full    Unzipped	Zipped File
2017-01 	14.5 MB	    39.1 GB	  7.8 GB
2017-02	  13.8 MB	    35.0 GB	  7.0 GB
2017-03	  12.3 MB	    39.5 GB	  7.9 GB
2017-04	  12.3 MB	    39.3 GB	  7.6 GB
2017-05	  13.4 MB	    40.7 GB	  7.3 GB
2017-06	  23.1 MB	    41.0 GB	  7.4 GB
2017-07	  16.5 MB	    51.0 GB	  7.8 GB
2017-08	  16.9 MB	    48.2 GB	  7.9 GB
2017-09	  14.7 MB	    47.2 GB	  7.8 GB
2017-10	  11.8 MB	    52.5 GB	  10.0 GB
2017-11	  10.6 MB	    54.5 GB	  10.0 GB
2017-12	  11.3 MB	    54.8 GB	  7.6 GB

*Processed file sizes are on the above.*

My first analyze was identifying keywords that might indicate hate speech in comments. Hate speech lexicon identified as;
“latino, arab, negroe, mexican, homo, homosexual, nigger, muslim,jewish, jew”
Above keywords had been searched in Pushshift API to define top 10 subreddits that includes most comment which includes those keywords. Pushshift API documentation can be found in “https://github.com/pushshift/api”, it is designed and created to help provide enhanced functionality and search capabilities for searching Reddit comments and submissions. This RESTful API gives full functionality for searching Reddit data and also includes the capability of creating powerful data aggregations. With this API, I was able to quickly find the data that is related with this project. 
Steps for searching in API;

1.  Search every given keyword through a for loop separately
2.  Get the number of comments that includes respected keyword and its subreddits
3.  Sort subreddits to find top 10 subreddit for corresponding keyword.
4.  Acquire all top 10 subreddits that includes hate speech keywords and choose 10 of the most anticipating ones (Exclude global subreddits such as “AskReddit”).

As a result of above analyze, I had acquired below list of subreddits that might be the most related subreddits to hate speech;

“4chan4trump, BlackPeopleTwitter, Catholicism, DebateFascism, The_Donald, askgaybros, exmuslim, milliondollarextreme, dankmemes, ImGoingToHellForThis”

Now, we have the subreddits and hate speech keywords, the next step is filtering big JSON files to those subreddits and keywords to reduce the dataset into a hate speech data. I had been used “JQ” to filter JSON files. JQ is a command line processor to slice and filter and map and transform structured data of JSON files. My output from JQ filtering process was .txt to easily implement as a python data frame. All of the computing and storing had been processed on Amazon Web Services. I had used EC2 for cloud computing and S3 for storing big files.

To sum up the process, steps in the data processing explained in the below;

1. Download the .bz file from pushshift.io website for every month of 2017 through bash script to EC2 Amazon Web Services’ cloud computing.
2. Unzip the file through bzip2 package in Unix shell to acquire compressed JSON file.
3. Filter related JSON file through JQ to have hate speech dataset and store it on S3 buckets.	
