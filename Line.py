from linebot import LineBotApi
from linebot.models import TextSendMessage
from linebot.exceptions import LineBotApiError

class LinePost:

    def __init__(self):
        with open('line_token.json','r') as f:
            json_load = json.load(f)

            YOUR_CHANNEL_ACCESS_TOKEN = json_load["YOUR_CHANNEL_ACCESS_TOKEN"]
            self.USER_ID = json_load["USER_ID"]

        self.api = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)

    def MsgPost(self,msg):
        messages = TextSendMessage(text=msg)
        self.api.push_message(self.USER_ID, messages=messages)

if __name__ == "__main__":
    post = LinePost()
    post.MsgPost("Hello Line!")
