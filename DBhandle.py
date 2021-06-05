import sqlite3

class DBHandle:

    # コンストラクタ
    def __init__(self,DBPATH):

        # データベースへの接続
        self.con = sqlite3.connect(DBPATH)
        self.cursor = self.con.cursor()

        # データベース作成
        try:
            # テーブル作成
            self.cursor.execute("CREATE TABLE IF NOT EXISTS article (id TEXT PRIMARY KEY, title TEXT)")
        except sqlite3.Error as e:
            print('Database error')
        
    # db内の記事取得用メソッド
    def GetArticleInfo(self):
        self.cursor.execute("SELECT * FROM article")
        article_id = self.cursor.fetchall()
        return [n for n in article_id]
    
    # 記事の登録用メソッド
    def PostArticleInfo(self,article_info):
        line = "INSERT INTO article VALUES (?,?)"
        self.cursor.execute(line,(article_info["id"],article_info["title"]))
        self.con.commit()

    # データベースクローズメソッド
    def CloseDB(self):
        self.con.close()