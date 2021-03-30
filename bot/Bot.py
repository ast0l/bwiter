from twitter.User import User
from notification.Notification import Notification
from threading import Timer


class Bot:
    def __init__(self, refresh_time: int = 30):
        self.__notify: Notification = Notification()
        self.__user: User = User()
        self.__refresh_time: int = refresh_time if refresh_time >= 30 else 30
        self.__run: bool = False

    def search_tweet(self):
        """
        launch the bot for searching new tweet each x second on
        the specified account
        :return:
        """
        # check if bot is not running to display notification run
        if not self.__run:
            self.status_run()

        print('search...')
        tweet: dict = self.__user.last_tweet()

        # check if tweet is new to display notification
        if tweet['new']:
            print('new tweet found')
            self.__notify.tweet(name=tweet['name'], desc=tweet['desc'])
        else:
            print('nothing new')
        Timer(self.__refresh_time, self.search_tweet).start()

    def status_run(self):
        self.__notify.bot_status('run')
        self.__run = True

    def status_stop(self):
        self.__notify.bot_status('stop')
        self.__run = False

    def set_user_to_track(self):
        """
        set the user to track
        :return:
        """
        name: input = input('who i have to track: ')
        while name == '':
            name: input = input('who i have to track: ')
        self.__notify.user(name=name)
        self.__user.screen_name = name
