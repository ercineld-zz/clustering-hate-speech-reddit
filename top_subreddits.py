import requests
import datetime as dt
import pandas as pd

#Get Subreddits that includes specific keywords via Reddit API(https://github.com/pushshift/api)
def get_api_request(word):
    start_epoch=int(dt.datetime(2017, 1, 1).timestamp())
    stop_epoch = int(dt.datetime(2018, 1, 1).timestamp())
    r = requests.get("https://api.pushshift.io/reddit/search/comment/?q="+ str(word) + "&after="+ str(start_epoch) + "&before=" + str(stop_epoch) + "&aggs=subreddit&size=0&limit100")
    r = r.json()
    r = r['aggs']
    r = r['subreddit']
    df = pd.DataFrame(r)
    df.sort_values(by='doc_count', ascending=False, inplace=True)
    df.columns = ['Frequency','Subreddit']
    df['Keyword'] = word
    return df

#Apply API results for specific hate speech keywords
def get_results():
    result = []
    search_words = ['latino', 'arab', 'negroe', 'mexican', 'homo'
                , 'homosexual', 'nigger', 'muslim', 'jewish', 'jew', 'bitch']
    for word in search_words:
        result.append(get_api_request(word))
    return result

#Data munging for top subreddits that includes hate speech keywords
def final_subreddits():
    result = get_results()
    subreddit = []
    for results in result:
        subreddit.append(results)
    df = pd.concat(subreddit)
    df = pd.pivot_table(df, values='Frequency'
                        ,index=('Keyword','Subreddit'),aggfunc='sum')
    df.reset_index(inplace=True)
    df.sort_values(by=['Keyword','Frequency'],inplace=True, ascending=False)
    return df

#Get the final data munging
def final_func():
    df = final_subreddits()
    search_words = ['latino', 'arab', 'negroe', 'mexican', 'homo'
                    , 'homosexual', 'nigger', 'muslim', 'jewish', 'jew', 'bitch']
    final = []
    for word in search_words:
        final.append(df[df.Keyword == word].head(10))
    data = pd.concat(final)
    data = list(set(data.Subreddit))
    return data

#Action!
subreddits = final_func()