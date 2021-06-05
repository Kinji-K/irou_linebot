from DBhandle import DBHandle
from GetUpdate import GetUpdate
from Line import LinePost

def compare(present_articles, db_articles):
    new_articles = []
    flug = 0

    for present_article in present_articles:
        for db_article in db_articles:
            flug = 0
            if present_article == db_article:
                flug = 1
                break
        
        if flug == 0:
            new_articles.append(present_article)
    
    return new_articles

def main():

    # 配列宣言
    db_articles = []

    # 最新記事の確認
    update = GetUpdate()
    present_articles = update.CheckUpdate()

    # dbの確認
    db = DBHandle("article.db")
    db_article_infos = db.GetArticleInfo()
    for n in db_article_infos:
        db_articles.append({
            "id": n[0],
            "title": n[1]
        })

    # 新規記事の抽出
    new_articles = compare(present_articles, db_articles)

    # 新規記事のDBへの登録
    for new_article in new_articles:
        db.PostArticleInfo(new_article)
    
    db.CloseDB()

    # 新規投稿がある場合
    if new_articles:

        # Line投稿用のメッセージ作成
        message = "新たな記事が投稿されました。"
        for article in new_articles:
            message = message + "\n\n" + article["title"] + "\n" + "https://iro-doku.com/archives/" + article["id"]

        line = LinePost()
        line.MsgPost(message)

if __name__ == "__main__":
    main()