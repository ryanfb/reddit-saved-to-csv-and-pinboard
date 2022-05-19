#! python3
# reddit_saved_to_csv.py - Exports your saved Posts and Comments on Reddit to a csv file.
import praw, csv, codecs, requests
from time import sleep

client_id='' # Enter your client ID
client_secret='' # Enter your client secret
username='' # Enter reddit username
password='' # Enter reddit password
pinboard_token='' # Pinboard API key e.g. username:1341235
pinboard_tags='reddit_saved' # Tags used for Pinboard

reddit = praw.Reddit(client_id=client_id,
                    client_secret=client_secret,
                    user_agent='Saved posts scraper by /u/' + username,
                    username=username,
                    password=password)

reddit_home_url = 'https://www.reddit.com'

saved_models = reddit.user.me().saved(limit=None) # models: Comment, Submission

reddit_saved_csv = codecs.open('reddit_saved.csv', 'w', 'utf-8') # creating our csv file

# CSV writer for better formatting
saved_csv_writer = csv.writer(reddit_saved_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
saved_csv_writer.writerow(['ID', 'Name', 'Subreddit', 'Type', 'URL', 'NoSFW']) # Column names

def handle(saved_models):
    count = 1
    for model in saved_models:
        subreddit = model.subreddit # Subreddit model that the Comment/Submission belongs to
        subr_name = subreddit.display_name
        url = reddit_home_url + model.permalink

        if isinstance(model, praw.models.Submission): # if the model is a Submission
            title = model.title
            noSfw = str(model.over_18)
            model_type = "#Post"
        else: # if the model is a Comment
            title = model.submission.title
            noSfw = str(model.submission.over_18)
            model_type = "#Comment"

        saved_csv_writer.writerow([str(count), title, subr_name, model_type, url, noSfw])
        print('Model number ' + str(count) + ' is written to csv file.')

        pinboard_params = {'description': title,
                           'url': url,
                           'tags': pinboard_tags,
                           'auth_token': pinboard_token}

        pinboard_response = requests.get('https://api.pinboard.in/v1/posts/add',
                                         params=pinboard_params,
                                         headers={'user-agent': 'reddit_saved_to_pinboard.py'})
        print('Model number ' + str(count) + ' saved to pinboard with response: ' + str(pinboard_response.status_code))
        sleep(3)

        count += 1

handle(saved_models)
reddit_saved_csv.close()

print("\nCOMPLETED!")
print("Your saved posts are available in reddit_saved.csv file.")
