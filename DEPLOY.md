# 🚀 デプロイ手順

## 1️⃣ GitHubリポジトリの作成

1. [GitHub](https://github.com/new) にアクセス
2. リポジトリ名: `sukiyaki-goku` (任意)
3. Public/Private を選択
4. **「Add a README file」のチェックは外す**（既にローカルにあるため）
5. 「Create repository」をクリック

## 2️⃣ ローカルとGitHubの接続

作成したリポジトリのURLをコピーして、以下のコマンドを実行：

```bash
# GitHubリポジトリのURLを設定（例）
git remote add origin https://github.com/YOUR_USERNAME/sukiyaki-goku.git

# ブランチ名をmainに変更（推奨）
git branch -M main

# GitHubにプッシュ
git push -u origin main
```

## 3️⃣ Cloudflare Pagesの設定

1. [Cloudflare Dashboard](https://dash.cloudflare.com/) にログイン
2. 「Workers & Pages」→「Pages」→「Create a project」
3. 「Connect to Git」を選択
4. GitHubアカウントを接続
5. 作成したリポジトリ（`sukiyaki-goku`）を選択
6. ビルド設定：
   - **Framework preset**: None
   - **Build command**: (空欄)
   - **Build output directory**: `/`
   - **Root directory**: `/`
7. 「Save and Deploy」をクリック

## 4️⃣ カスタムドメインの設定（オプション）

既存のドメイン `sukiyakigoku.pages.dev` を使用する場合：

1. Cloudflare Pages プロジェクト設定
2. 「Custom domains」タブ
3. 既存のプロジェクトを削除して、新しいプロジェクトに紐付け

---

## ✅ 完了後の確認

- https://sukiyakigoku.pages.dev/ にアクセス
- ページが正しく表示されることを確認
- 画像が全て読み込まれることを確認
- モバイル表示の確認

## 🔄 今後の更新方法

```bash
# ファイルを編集後
git add .
git commit -m "Update: 変更内容"
git push

# Cloudflare Pagesが自動でデプロイ（約1分）
```

---

## 📝 現在のファイル構成

```
/
├── index.html          # メインHTML
├── assets/
│   └── img/           # 画像ファイル（13枚）
├── README.md
├── .gitignore
└── DEPLOY.md          # このファイル
```
