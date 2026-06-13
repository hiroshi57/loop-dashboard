# DI Loop Library 1000 — ダッシュボード構築プロンプト

> このファイルを Claude Code にそのまま渡してください。
> 同梱の `loops_1000.json`（1,000本のエージェントループのデータセット）を同じディレクトリに置いた状態で実行してください。

---

## あなた（Claude Code）への指示

あなたはフロントエンドエンジニアです。同じディレクトリにある `loops_1000.json` を読み込み、**1,000本のエージェントループを閲覧・検索・コピーできるダッシュボード**を構築してください。

### 背景

- ループのフォーマットは https://loops.elorm.xyz/loops を踏襲しています（Goal / Max iterations / Between iterations run / Exit when / Step 1 / Self-pace 指示で構成される「キックオフプロンプト」形式）。
- 1,000本のループは、株式会社デジタルアイデンティティのサービス分類（https://digitalidentity.co.jp/service/ ）に基づく **16サービス**に分類されています。

### データ構造（loops_1000.json）

```jsonc
{
  "meta": { "name", "description", "totalLoops": 1000, ... },
  "services": [ { "key", "name", "description", "loopCount" }, ... ],  // 16件
  "categories": ["Quality", "Performance", "Review", "Automation", "Docs"],
  "triggers": ["manual", "interval"],
  "loops": [
    {
      "id": "seo-02-fix",
      "title": "内部リンク構造最適化｜改善ループ",
      "service": "SEO",
      "serviceKey": "seo",
      "category": "Quality",          // Quality | Performance | Review | Automation | Docs
      "trigger": "manual",            // manual | interval
      "goal": "...",
      "maxIterations": 10,
      "checkCommand": "...",          // Between iterations run に相当
      "exitCondition": "...",         // Exit when に相当
      "step1": "...",
      "tags": ["seo", "improvement", "marketing"],
      "agents": ["Claude Code", "Cursor"],
      "kickoffPrompt": "Start the \"...\" loop.\n\nGoal: ...\n..."  // そのままコピーして使える完成形
    },
    ...  // 全1,000件
  ]
}
```

16サービス: 全体戦略 / AD／デジタル広告 / SEO / 制作 / マーケティングDX / コンテンツマーケティング / WEB解析 / SNS・PR / CMO代行 / 事業承継 / インハウス支援 / 金融チーム / 不動産チーム / WordPress / 薬機法・医師監修 / Forté.AI

### 技術要件

1. **単一の `index.html`**（HTML + CSS + Vanilla JS、ビルド不要）で実装すること。外部ライブラリは CDN 可（Chart.js 推奨）。
2. `fetch('./loops_1000.json')` でデータを読み込むこと。`file://` では fetch が失敗するため、READMEに `python3 -m http.server` 等での起動方法を記載すること（あるいは起動スクリプトを用意）。
3. 1,000件をすべてDOMに描画しない。**ページネーション（24件/ページ）または仮想スクロール**で軽快に動作させること。
4. レスポンシブ対応（モバイル1カラム / デスクトップ3カラム程度）。
5. ダークモード切り替えがあると望ましい（任意）。

### ダッシュボード要件

#### ① サマリーセクション（最上部）
- 総ループ数（1,000）、サービス数（16）、カテゴリ数、トリガー種別数のKPIカード
- **サービス別ループ数の横棒グラフ**（16サービス、クリックでそのサービスにフィルタ）
- **カテゴリ別の構成比ドーナツグラフ**（Quality / Performance / Review / Automation / Docs）
- トリガー別（manual / interval）の内訳表示

#### ② フィルタ＆検索バー
- サービス（16択 + すべて）— チップまたはセレクト
- カテゴリ（5択 + すべて）
- トリガー（manual / interval / すべて）
- フリーワード検索（title / goal / tags / step1 を対象、インクリメンタル）
- 適用中フィルタの表示とワンクリック解除、該当件数の表示

#### ③ ループカード一覧
loops.elorm.xyz のカードを参考に、各カードへ以下を表示:
- カテゴリバッジ・トリガーバッジ・サービスバッジ（サービスごとに色分け）
- タイトル、Goal（要約として表示）
- Max iterations / Exit when の要点
- タグ、対応エージェント
- **「Copy」ボタン**: `kickoffPrompt` をクリップボードにコピーし、「Copied!」のフィードバックを表示
- **「View」**: クリックでモーダル（または展開）を開き、kickoffPrompt 全文を等幅フォントで表示＋コピーボタン

#### ④ サービス別ビュー
- サマリーのグラフまたはサービスチップから遷移し、サービス単体の内訳（カテゴリ分布・ループ一覧）が見られること

### 完了条件（あなた自身がこのループの exit condition として使うこと）

```
Goal: ダッシュボードがブラウザで正しく表示・操作できる
Max iterations: 8
Between iterations run: ローカルサーバーで index.html を開き、フィルタ・検索・コピー・グラフ操作を確認
Exit when:
  - 1,000件すべてがフィルタ・検索の対象になっている
  - サービス16分類のフィルタとグラフ連動が機能する
  - Copyボタンで kickoffPrompt がコピーできる
  - コンソールエラーがゼロ
Step 1: index.html の骨格（データ読み込み＋カード描画＋ページネーション）を実装して動作確認する。

Self-pace this loop. 各イテレーション後にチェックを実行し、終了条件を満たしていない場合のみ継続すること。
```

### 成果物
- `index.html`（ダッシュボード本体）
- `README.md`（起動方法: 例 `python3 -m http.server 8000` → http://localhost:8000）

---

## 付録: ループデータの構成ロジック（参考）

- 各サービスに13の業務テーマ（例: SEO → テクニカルSEO監査、内部リンク構造最適化、LLMO・AI検索最適化 など）を定義
- 各テーマに5つのループパターンを掛け合わせて生成:

| パターン | トリガー | カテゴリ | Max iter | 概要 |
|---|---|---|---|---|
| 改善ループ | manual | Quality | 10 | 課題を洗い出し、1件ずつ修正して課題ゼロまで回す |
| 閾値達成ループ | manual | Performance | 12 | KPIを計測し、目標閾値に到達するまで施策を1つずつ実行 |
| 監査パス | manual | Review | 8 | チェックリストを未完了ゼロまで消化 |
| 定期モニタリング | interval | Automation | 20 | 状態を定期取得し、異常があれば一次対応 or エスカレーション |
| レポート整備ループ | manual | Docs | 4 | ドラフト→3観点の自己レビュー→修正をレビュー通過まで反復 |

- 配分: 先頭8サービス × 63本 + 後半8サービス × 62本 = **1,000本**
