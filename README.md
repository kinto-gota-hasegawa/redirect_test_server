# リダイレクトを簡単にテストするテストサーバー

> [!IMPORTANT]
> [こちら](https://www.lifewithpython.com/2021/03/python-https-server.html)を下に、同じフォルダ内に、自己証明書を配置する必要があります。

> [!IMPORTANT]
> 自己証明書を仕様しているためSslエラーはスキップする必要があります。
> ```kt
> override fun onReceivedSslError(view: WebView?, handler: SslErrorHandler?, error: SslError?) {
>   handler?.proceed()
> }
> ```

### アクセス先のURL

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




# 参考

- pythonでhttpsサーバーを作る
  - https://www.lifewithpython.com/2021/03/python-https-server.html
