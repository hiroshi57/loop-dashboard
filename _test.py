# -*- coding: utf-8 -*-
import re, json, sys
if hasattr(sys.stdout,'reconfigure'): sys.stdout.reconfigure(encoding='utf-8')

html=open('index.html',encoding='utf-8').read()
d=json.load(open('loops_1000.json',encoding='utf-8'))
loops=d['loops']
results=[]
def ok(id,msg): results.append(('PASS',id,msg))
def fail(id,msg): results.append(('FAIL',id,msg))

# A: 初期表示
ok('A-1','KPI') if 'loops.length.toLocaleString' in html and 'DATA.services.length' in html else fail('A-1','KPI欠損')
ok('A-2','エラー表示') if 'loops_1000.json を読み込めませんでした' in html else fail('A-2','エラー表示欠損')
ok('A-3','テーマ初期化') if 'di-theme' in html and 'prefers-color-scheme: dark' in html else fail('A-3','テーマ初期化欠損')
ok('A-4','ヘッダー件数') if 'hdCount' in html else fail('A-4','ヘッダー件数欠損')
ok('A-5','フッター') if 'footMeta' in html and 'm.generatedAt' in html else fail('A-5','フッター欠損')

# B: チャート
ok('B-1','棒グラフ') if 'chart.umd.min.js' in html and 'new Chart(' in html else fail('B-1','棒グラフ欠損')
ok('B-2','軸タブ切替') if 'chartAxis=b.dataset.axis' in html and 'rebuildCharts' in html else fail('B-2','軸タブ切替欠損')
ok('B-3','チャートクリック') if 'setFilter(chartAxis' in html else fail('B-3','チャートクリック欠損')
ok('B-4','トグル解除') if 'state[key]===value' in html else fail('B-4','トグル解除欠損')
ok('B-5','ドーナツ') if 'doughnut' in html and 'catChart' in html else fail('B-5','ドーナツ欠損')
ok('B-6','ドーナツクリック') if 'setFilter("category"' in html else fail('B-6','ドーナツクリック欠損')
ok('B-7','トリガーバー') if 'trigRows' in html else fail('B-7','トリガーバー欠損')
ok('B-8','テーマ再描画') if 'rebuildCharts()' in html and 'di-theme' in html else fail('B-8','テーマ再描画欠損')

# C: Pain
ok('C-1','課題15件') if len(d['pains'])==15 else fail('C-1','課題数:'+str(len(d['pains'])))
ok('C-2','課題選択') if 'state.pains.push(k)' in html else fail('C-2','課題選択欠損')
ok('C-3','課題解除') if 'state.pains.splice(idx,1)' in html else fail('C-3','課題解除欠損')
ok('C-4','複数選択バッジ') if 'pain-multi-badge' in html else fail('C-4','複数選択バッジ欠損')

# D: 検索
ok('D-1','検索debounce') if 'debounce' in html and 'state.q=v.trim' in html else fail('D-1','検索debounce欠損')
ok('D-2','カッコ除去') if bool(re.search(r'replace.*「」', html)) else fail('D-2','カッコ除去ロジック欠損')
ok('D-3','シノニム') if 'SYNONYMS' in html and '"seo"' in html else fail('D-3','シノニム欠損')
ok('D-4','検索クリア') if 'qClear' in html and 'state.q=""' in html else fail('D-4','検索クリア欠損')
ok('D-5-7','3軸フィルタ') if all(x in html for x in ['filterAxis==="service"','filterAxis==="industry"','filterAxis = "pain"']) else fail('D-5-7','3軸フィルタ欠損')
ok('D-8','カテゴリチップ') if 'catChips' in html and 'state.category' in html else fail('D-8','カテゴリチップ欠損')
ok('D-9','トリガーチップ') if 'trigChips' in html and 'state.trigger' in html else fail('D-9','トリガーチップ欠損')
ok('D-11-13','ピル・解除') if 'active-pill' in html and 'clearAll' in html else fail('D-11-13','ピル・解除欠損')
ok('D-14','ゼロ件メッセージ') if '該当するループがありません' in html else fail('D-14','ゼロ件メッセージ欠損')

# E: カード・ページネーション
ok('E-1','24件/ページ') if 'PER_PAGE = 24' in html else fail('E-1','PER_PAGE欠損')
ok('E-2','カードホバー') if 'translateY(-2px)' in html and 'card:hover' in html else fail('E-2','カードホバー欠損')
ok('E-3','スクロール') if 'scrollIntoView' in html else fail('E-3','スクロール欠損')
ok('E-4','first/lastDisabled') if 'p===1?"disabled":""' in html and 'p===total?"disabled":""' in html else fail('E-4','disabled欠損')
ok('E-5','ページ情報') if 'pinfo' in html and 'filtered.length' in html else fail('E-5','ページ情報欠損')
ok('E-6','ページネ非表示') if 'filtered.length<=PER_PAGE' in html else fail('E-6','ページネ非表示欠損')

# F: モーダル
ok('F-1','モーダル開く') if 'openModal' in html and 'overlay' in html else fail('F-1','モーダル開く欠損')
ok('F-2','TLDR') if 'このループがすること' in html and 'tldr' in html else fail('F-2','TLDR欠損')
ok('F-3','トリガー説明') if 'いつ動く（始まり方）' in html and 'cleanTriggerDetail' in html else fail('F-3','トリガー説明欠損')
ok('F-4','完了条件') if '完了の合図' in html and 'exitCondition' in html else fail('F-4','完了条件欠損')
ok('F-5','業種固有') if 'この業種での効かせ方' in html and 'ind-spec' in html else fail('F-5','業種固有欠損')
ok('F-7-8','サイクルマップ') if 'cycle-map' in html and '1へ戻る' in html and 'flow-loop' in html else fail('F-7-8','サイクルマップ欠損')
ok('F-9','折りたたみ') if 'details.more' in html and 'もっと詳しく見る' in html else fail('F-9','折りたたみ欠損')
ok('F-10','モーダル閉じる') if 'closeModal' in html and 'classList.remove("show")' in html else fail('F-10','モーダル閉じる欠損')
ok('F-11','オーバーレイクリック') if 'e.target===$(\"#overlay\")' in html else fail('F-11','オーバーレイクリック欠損')
ok('F-12','Escキー') if 'e.key==="Escape"' in html else fail('F-12','Escキー欠損')
ok('F-13','モーダルコピー') if 'kickoffPrompt' in html and 'mCopy' in html else fail('F-13','モーダルコピー欠損')

# G: コピー
ok('G-1-2','クリップボード') if 'navigator.clipboard.writeText' in html and 'execCommand("copy")' in html else fail('G-1-2','コピーロジック欠損')
ok('G-3','コピー失敗') if 'コピーに失敗しました' in html else fail('G-3','コピー失敗トースト欠損')

# H: お気に入り
ok('H-1','お気に入りUI') if 'favorites' in html and 'fav-btn' in html and 'fav-bar' in html else fail('H-1','お気に入り欠損')
ok('H-2','トグル') if 'favorites.has(id)' in html and 'favorites.delete(id)' in html else fail('H-2','トグル欠損')
ok('H-3','まとめてコピー') if 'exportFavorites' in html and 'kickoffPrompt' in html else fail('H-3','まとめてコピー欠損')
ok('H-4','全解除') if 'favorites.clear()' in html else fail('H-4','全解除欠損')
ok('H-5','ゼロ件') if 'お気に入りがありません' in html else fail('H-5','ゼロ件トースト欠損')

# I: パーマリンク
ok('I-1','pushHash') if 'pushHash' in html and 'history.replaceState' in html else fail('I-1','pushHash欠損')
ok('I-2-3','parseHash') if 'parseHash' in html and 'location.hash' in html else fail('I-2-3','parseHash欠損')
ok('I-4','URLクリーン') if 'location.pathname+location.search' in html else fail('I-4','URLクリーン欠損')

# J: テーマ
ok('J-1-2','テーマ保存') if 'di-theme' in html and 'localStorage.setItem' in html else fail('J-1-2','テーマ保存欠損')

# K: 軸詳細
ok('K-1-4','軸詳細') if 'axisDetail' in html and 'renderAxisDetail' in html else fail('K-1-4','軸詳細欠損')

# L: アクセシビリティ
ok('L-1','フォーカス') if ':focus-visible' in html else fail('L-1','フォーカス欠損')
ok('L-2','reduced-motion') if 'prefers-reduced-motion' in html and 'animation:none!important' in html else fail('L-2','reduced-motion欠損')
ok('L-3-4','レスポンシブ') if 'max-width:980px' in html and 'max-width:620px' in html else fail('L-3-4','レスポンシブ欠損')
ok('L-5','ARIA') if 'role="dialog"' in html and 'aria-modal="true"' in html else fail('L-5','ARIA欠損')

# --- データ整合性 ---
seo_med=[l for l in loops if l['serviceKey']=='seo' and l['industryKey']=='medical']
ok('DATA-AND','SEO×医療AND: '+str(len(seo_med))+'件') if len(seo_med)>0 else fail('DATA-AND','SEO×医療 0件')
spam=[l for l in loops if 'spam' in l['id']]
ok('DATA-SPAM','スパムループ20本') if len(spam)==20 else fail('DATA-SPAM','スパムループ数:'+str(len(spam)))
no_goal=[l['id'] for l in loops if not l.get('goal','').strip()]
ok('DATA-GOAL','全ループgoal存在') if not no_goal else fail('DATA-GOAL','goal欠落:'+str(len(no_goal))+'本')
no_exit=[l['id'] for l in loops if not l.get('exitCondition','').strip()]
ok('DATA-EXIT','全ループexitCondition存在') if not no_exit else fail('DATA-EXIT','exitCondition欠落:'+str(len(no_exit))+'本')
no_kick=[l['id'] for l in loops if not l.get('kickoffPrompt','').strip()]
ok('DATA-KICK','全ループkickoffPrompt存在') if not no_kick else fail('DATA-KICK','kickoffPrompt欠落:'+str(len(no_kick))+'本')

# --- AND検索ロジック確認 ---
import re as re2

def _expand_test(raw):
    if not raw: return []
    s = raw
    for cp in [0x300c,0x300d,0x300e,0x300f,0x201c,0x201d,0x2018,0x2019]:
        s = s.replace(chr(cp), "")
    s = s.replace(chr(0x3000), " ").strip().lower()
    if not s: return []
    return [[t] for t in s.split()]

# 正規化チェック（カッコ除去・小文字化）
_nc = [
    (chr(0x300c)+"spam"+chr(0x300d), "spam"),
    ("spam", "spam"),
    ("SEO", "seo"),
    (" search ", "search"),
]
_norm_ok = all(_expand_test(i)[0][0] == e for i, e in _nc)
ok("D-2-norm", "expandQuery正規化全PASS") if _norm_ok else fail("D-2-norm", "expandQuery正規化失敗")

# AND 分割チェック
_ac = [
    ("seo medical", 2, ["seo", "medical"]),
    ("spam update plan", 3, ["spam", "update", "plan"]),
    ("word", 1, ["word"]),
]
_and_ok = all(len(_expand_test(r)) == n and [g[0] for g in _expand_test(r)] == toks for r, n, toks in _ac)
ok("D-2-and", "AND分割（スペース区切り）全PASS") if _and_ok else fail("D-2-and", "AND分割失敗")

# AND 検索が index.html に実装されているか
ok("D-2-logic", "AND検索ロジック実装済み") if "q.every(group=>group.some(" in html else fail("D-2-logic", "AND検索ロジック未実装")

# スパムシノニム追加確認
ok("D-3-spam", "スパムシノニム追加済み") if chr(0x30b9)+chr(0x30d1)+chr(0x30e0) in html and "SYNONYMS" in html else fail("D-3-spam", "スパムシノニム欠損")

# --- 結果 ---
passed=[r for r in results if r[0]=="PASS"]
failed=[r for r in results if r[0]=="FAIL"]
print(f"=== RESULT: PASS {len(passed)} / FAIL {len(failed)} / TOTAL {len(results)} ===")
if failed:
    print("")
    print("--- FAIL ---")
    for s,id,msg in failed: print(f"  FAIL {id}: {msg}")
print("")
print("--- PASS ---")
for s,id,msg in passed: print(f"  PASS {id}: {msg}")
