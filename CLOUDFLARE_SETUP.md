# 🚀 Cloudflare Pages デプロイ設定ガイド

## ✅ 現在の状態
- ✅ GitHubリポジトリ: https://github.com/OJBeert/sukiyakigoku
- ✅ ローカルコミット完了
- ✅ GitHubへのプッシュ完了

## 📋 Cloudflare Pages設定手順

### ステップ1: Cloudflare Dashboardにアクセス

1. https://dash.cloudflare.com/ を開く
2. ログイン（アカウントがない場合は作成）

### ステップ2: 新しいプロジェクトを作成

1. **左メニュー** → **「Workers & Pages」**
2. **「Pages」タブ** をクリック
3. **「Create a project」** をクリック

### ステップ3: GitHubリポジトリを接続

1. **「Connect to Git」** を選択
2. **「GitHub」** を選択
3. GitHubアカウントを接続（初回のみ）
4. **リポジトリを選択**: `OJBeert/sukiyakigoku`
5. **「Begin setup」** をクリック

### ステップ4: ビルド設定を構成

以下の設定を入力：

```
Project name: sukiyaki-goku （任意）
Production branch: main

Build settings:
  Framework preset: None
  Build command: (空欄のまま)
  Build output directory: /
  Root directory: (空欄のまま)

Environment variables: (不要)
```

### ステップ5: デプロイ

1. **「Save and Deploy」** をクリック
2. デプロイが開始（約1-2分）
3. デプロイ完了を待つ

### ステップ6: カスタムドメイン設定（重要）

既存の `sukiyakigoku.pages.dev` を使用する場合：

1. デプロイ完了後、プロジェクト設定を開く
2. **「Custom domains」** タブ
3. **「Set up a custom domain」** をクリック
4. `sukiyakigoku.pages.dev` を入力
5. 既存のプロジェクトがある場合は削除して紐付け

---

## ✅ デプロイ完了後の確認

デプロイ完了後（約1-2分）、以下を確認してください：

### 1. ページが表示されるか確認
```
https://sukiyakigoku.pages.dev/
```

### 2. 画像が全て読み込まれているか確認
- ブラウザの開発者ツール（F12）→ Network タブ
- 画像ファイル（assets/img/*.jpeg）が全て200で読み込まれているか確認

### 3. 機能確認
- ✅ ナビゲーション（メニュー）が動作
- ✅ 言語切り替え（日本語/English）が動作
- ✅ 予約ボタンのリンクが機能
- ✅ モバイル表示が正常

### 4. SEO確認
```
ページソースを表示（Ctrl+U または Cmd+U）
以下が含まれているか確認：
- <title>WAGYU SUKIYAKI 極〜GOKU〜 | 東銀座・築地...
- <meta name="description" content="...
- <meta property="og:title" content="...
- <meta property="og:image" content="...
```

---

## 🆘 トラブルシューティング

### エラー: 404 Not Found
**原因**: Build output directory が正しくない

**解決方法**:
1. プロジェクト設定 → Build settings
2. Build output directory を `/` に設定
3. 再度デプロイ

### エラー: 画像が表示されない
**原因**: 画像パスが正しくない

**確認方法**:
1. ブラウザの開発者ツール → Network タブ
2. 画像ファイルのリクエストを確認
3. 404エラーが出ていないか確認

**解決方法**:
```html
<!-- 正しいパス -->
<img src="assets/img/hero-bg.jpeg">

<!-- 間違ったパス -->
<img src="/assets/img/hero-bg.jpeg">  <!-- ❌ -->
<img src="./assets/img/hero-bg.jpeg"> <!-- ❌ -->
```

### エラー: デプロイが失敗する
**確認方法**:
1. Cloudflare Pages → プロジェクト → Deployments
2. 失敗したデプロイをクリック
3. ログを確認

---

## 🔄 今後の更新方法

ファイルを編集後：

```bash
cd /Users/ojbeert/lp-system/templates/goku

# ファイルをステージング
git add .

# コミット
git commit -m "Update: 変更内容"

# プッシュ
git push
```

Cloudflare Pagesが自動でデプロイ（約1-2分）

---

## 📞 サポート

### Cloudflare Pages ドキュメント
- https://developers.cloudflare.com/pages/

### よくある質問
- **Q: デプロイに時間がかかる**
  - A: 初回は2-3分かかることがあります。Deployments タブで進捗を確認できます。

- **Q: 既存のドメインを使用したい**
  - A: Custom domains タブで設定できます。

- **Q: 環境変数を使用したい**
  - A: Build settings で Environment variables を設定できます。

---

## 📝 チェックリスト

- [ ] Cloudflare Dashboardにログイン
- [ ] 新しいプロジェクトを作成
- [ ] GitHubリポジトリを接続
- [ ] ビルド設定を構成
- [ ] デプロイを実行
- [ ] カスタムドメインを設定
- [ ] ページが表示されることを確認
- [ ] 画像が全て読み込まれることを確認
- [ ] 機能が正常に動作することを確認
