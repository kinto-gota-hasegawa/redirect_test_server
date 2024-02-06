# リダイレクトを簡単にテストするテストサーバー

特定のリダイレクトを検証するための簡易的なテストサーバーです。
AndroidなどのWebViewから本サーバーの`index.html`にアクセスしテキストリンクを押すことで、`redirect_url.txt`の1行目に定義したURLにリダイレクトさせることができます。
WebView上でDeepLinkが正しく動いていことの検証などに使用することができます。


# 実行手順

1. **証明書を作成**

[こちら](https://www.lifewithpython.com/2021/03/python-https-server.html)を参考にしました。
Androidではhttpsの通信しか許可していない場合が多いので、下記のコマンドで作成される`localhost.pem`をローカルのリポジトリトップに配置してください。
このファイルはgitの管理外です。
```
openssl req -x509 -new -days 365 -nodes \
  -keyout localhost.pem \
  -out localhost.pem \
  -subj "/CN=localhost"
```

2. **WebViewなどではSslErrorをスキップ**
   
もしAndroidのWebViewを使用しているSslErrorをスキップする必要があります。これは自己証明書を利用しているためです。
```kt
object : WebViewClient() {
    ...
    override fun onReceivedSslError(view: WebView?, handler: SslErrorHandler?, error: SslError?) {
        handler?.proceed()
    }
}
```

3. **`redirect_url.txt`を設定**

リダイレクト先として検証したいURLを`redirect_url.txt`の1行目に記載します。ここのファイルはgitの管理外です。
例えば以下のようにすると、googleの検索ページにリダイレクトします。
```
echo https://www.google.co.jp/ > redirect_url.txt
```


4. **`main.py`を実行**

`python main.py`を実行してください。
実行すると以下のアドレスから`index.html`にアクセスすることができます。


5. アクセスする先のURLは以下です。

- ブラウザの場合
```
https://localhost:8000/
```

- エミュレータの場合
```kt
https://10.0.2.2:8000/
```

- 実機の場合
→ 会社PCではportを開放できない


6. **表示されたリンクをクリックする**

画面中央上部に`Redirect to the URL of the top line in redirect_url.txt`というテキストリンクが表示されます。クリックするとリダイレクトします。

|<img width="1920" alt="image" src="https://github.com/kinto-gota-hasegawa/redirect_test_server/assets/112846158/cc7d26c6-dcdf-4cbf-bb96-382c1767c4c9">|
|:-:|

