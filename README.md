# twittercontrol
Allows people to use twitter to control python projects

## Setup and Test twittercontrol

1 - Install twython (https://github.com/ryanmcgrath/twython) with ```pip install twython```

2 - Go to https://projects.raspberrypi.org/en/projects/getting-started-with-the-twitter-api/2 and follow the instructions to create a twitter developer account

3 - Go to https://projects.raspberrypi.org/en/projects/getting-started-with-the-twitter-api/4 and follow the instructions to create a developer account - Make sure you can access the consumer, consumer secret, access token and access token secret keys!

4 - Download this GitHub repository into a folder on your computer

5 - Go into *twittercontrol.py* and copy and paste the consumer, consumer secret, access token and access token secret keys - don't forget to put in the twitter handle you want to check to see if someone has posted!

```python
twitterHandle='<your twitter handle>'
consumer_key = "<consumer api key>"
consumer_secret = "<consumer api secret key>"
access_token = "<access token key>"
access_token_secret = "<access token secret>"
```

6 - Then run *twittercontrol.py* and tweet from your account @your twitter handle What is your favourite single-board computer?
  
7 - The script should then print **Raspberry Pi 4** if it has worked

## Create your own action




