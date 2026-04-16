# 既存Cloudflare Pagesプロジェクトの再設定

## 📌 状況
既存の `sukiyakigoku.pages.dev` プロジェクトがあり、新しいプロジェクトを作成できない場合

## ✅ 解決方法

### オプション1: 既存プロジェクトを更新（推奨）

1. **Cloudflare Dashboard** → **Workers & Pages** → **Pages**
2. 既存の `sukiyakigoku` プロジェクトをクリック
3. **Settings** → **Build & Deployments**
4. **GitHub** セクションで以下を確認：
   - Repository: `OJBeert/sukiyakigoku`
   - Branch: `main`
5. 設定が正しければ、自動的にデプロイが開始される

### オプション2: 既存プロジェクトを削除して再作成

1. **既存プロジェクトを削除**:
   - プロジェクト設定 → **Delete project**
   - 確認して削除

2. **新しいプロジェクトを作成**:
   - **Create a project** → **Connect to Git**
   - `OJBeert/sukiyakigoku` を選択
   - Project name: `sukiyaki-goku-v2` （別の名前）
   - Build settings:
     - Framework preset: **None**
     - Build command: (空欄)
     - Build output directory: **/**
   - **Save and Deploy**

3. **カスタムドメインを設定**:
   - デプロイ完了後、**Custom domains**
   - `sukiyakigoku.pages.dev` を追加

---

## 🔍 デプロイ状況の確認

### Deployments タブで確認
1. プロジェクト → **Deployments**
2. 最新のデプロイを確認
3. ステータスが **Success** か **Failed** か確認

### ログを確認
1. 失敗したデプロイをクリック
2. **View build log** をクリック
3. エラーメッセージを確認

---

## 🆘 よくあるエラー

### エラー: Build failed
**原因**: ビルド設定が正しくない

**解決方法**:
- Build command: (空欄のまま)
- Build output directory: `/`

### エラー: Repository not found
**原因**: GitHubリポジトリへのアクセス権限がない

**解決方法**:
1. Cloudflare → Settings → GitHub
2. GitHub接続を再認証

### エラー: Custom domain already in use
**原因**: ドメインが別のプロジェクトに紐付いている

**解決方法**:
1. 古いプロジェクトのカスタムドメイン設定を削除
2. 新しいプロジェクトに追加

---

## 📞 サポート

問題が解決しない場合：
1. Cloudflare Pages ドキュメント: https://developers.cloudflare.com/pages/
2. GitHub Issues: https://github.com/OJBeert/sukiyakigoku/issues
