# ⚡ 最速デプロイ手順（5分で完了）

## 📌 現在の状態
✅ ローカルGitリポジトリ準備完了  
✅ SEO/OGP最適化済み  
✅ 画像外部化完了  

## 🚀 デプロイ手順（3ステップ）

### ステップ1: GitHubリポジトリ作成（1分）

1. **ブラウザで開く**: https://github.com/new
2. **設定**:
   - Repository name: `sukiyaki-goku`
   - Public/Private: どちらでもOK
   - ⚠️ **「Add a README file」のチェックを外す**
3. **「Create repository」をクリック**

### ステップ2: GitHubにプッシュ（1分）

リポジトリ作成後に表示される画面から、**「…or push an existing repository from the command line」**のコマンドをコピーして実行：

```bash
# 例（YOUR_USERNAMEは実際のユーザー名に置き換え）
git remote add origin https://github.com/YOUR_USERNAME/sukiyaki-goku.git
git branch -M main
git push -u origin main
```

または、このディレクトリで以下を実行：

```bash
cd /Users/ojbeert/lp-system/templates/goku

# GitHubで表示されたURLに置き換えて実行
git remote add origin https://github.com/YOUR_USERNAME/sukiyaki-goku.git
git push -u origin main
```

### ステップ3: Cloudflare Pagesでデプロイ（3分）

1. **Cloudflare Dashboardを開く**: https://dash.cloudflare.com/
2. **「Workers & Pages」→「Pages」→「Create a project」**
3. **「Connect to Git」を選択**
4. **GitHubアカウントを接続**（初回のみ）
5. **リポジトリを選択**: `sukiyaki-goku`
6. **ビルド設定**:
   ```
   Framework preset: None
   Build command: (空欄)
   Build output directory: /
   Root directory: (空欄)
   ```
7. **「Save and Deploy」をクリック**

### ステップ4: カスタムドメイン設定（オプション）

既存の `sukiyakigoku.pages.dev` を使用する場合：

1. デプロイ完了後、プロジェクト設定を開く
2. **「Custom domains」タブ**
3. **「Set up a custom domain」**
4. `sukiyakigoku.pages.dev` を入力
5. 既存のプロジェクトがある場合は削除して紐付け

---

## ✅ 完了確認

デプロイ完了後（約1分）、以下を確認：

- ✅ https://sukiyakigoku.pages.dev/ にアクセス
- ✅ ページが正しく表示される
- ✅ 画像が全て読み込まれる
- ✅ モバイル表示が正常
- ✅ 言語切り替えが動作

---

## 🔄 今後の更新方法

ファイルを編集後：

```bash
cd /Users/ojbeert/lp-system/templates/goku
git add .
git commit -m "Update: 変更内容"
git push
```

Cloudflare Pagesが自動でデプロイ（約1分）

---

## 🆘 トラブルシューティング

### エラー: `remote origin already exists`
```bash
git remote remove origin
git remote add origin https://github.com/YOUR_USERNAME/sukiyaki-goku.git
git push -u origin main
```

### エラー: `Permission denied (publickey)`
```bash
# HTTPSを使用（パスワード認証）
git remote set-url origin https://github.com/YOUR_USERNAME/sukiyaki-goku.git
git push -u origin main
```

### Cloudflare Pagesでページが表示されない
- Build output directory が `/` になっているか確認
- `index.html` がルートディレクトリにあるか確認
- デプロイログでエラーがないか確認

---

## 📞 サポート

問題が解決しない場合は、以下の情報を確認：
- GitHubリポジトリURL
- Cloudflare Pagesのデプロイログ
- ブラウザのコンソールエラー
