# ai-buildathon-2024-test

### starting command
make up

- オートリロードにはバインドマウントによって変更が反映されるようにする必要がある。
> バインドマウントの設定を行っている部分ですね。つまり、app直下のソースコードを編集すると、それを共有しているコンテナ内部のusr/src/app直下にあるファイルも書き換えられ、変更が反映される訳です。
https://zenn.dev/randd_inc/articles/84ac7de7f22800

- 注意：デプロイ時、Cloud Runの設定でポートを80に設定する。