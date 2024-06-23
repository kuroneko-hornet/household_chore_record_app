【Git ローカル編集からマージまでのフロー】

1. ローカル編集（ローカル作業）
    1. Visual Studio Codeを起動
    2. File > open Folder > プロジェクトフォルダ クリック
    3. Ctrl + J でGit bashターミナル起動
    4. git pull ※リモートの変更内容をローカルのmain branchに反映
    4. git switch -c <feature ブランチ名> ※ブランチを切る
    5. Python app.pyを実行
    6. コード編集・保存
    7. テスト

2. リモートへコミット（ローカル作業）
    ※ブランチがmainではないことを必ず確認すること
    1. git status    ※変更状況を確認
    2. git add <変更ファイル名>
    3. git commit -m <メッセージ内容>
    4. git log  ※メッセージ内容を確認する 
    5. git push

3. レビュー依頼（ブラウザ作業）
    1. Git Hubを表示し、Pull Request作成ボタンをクリック
    2. Purposeを入力
    3. Pull Request Typeに当てはまるものにチェック
    4. How to Testに変更内容とエビデンスを貼り付け
    5. Reviewersに担当者を選択する
    6. Create Pull requestをクリック

4. マージ（ブラウザ作業）
    1. Reviewerのレビュー完了後、コードが反映
    2. クラウドに反映完了後、ブラウザに変更される
    3. git switch main  ※マージを確認後、branchをmainに戻す

