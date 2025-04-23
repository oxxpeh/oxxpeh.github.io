# PyScript Editor動作できたのでちょっと比較
他で作ったyamlで図データ取得してplotlyで描画するやつで比較  
GithubpagesでCORP関連のヘッダ追加設定できなさそうなのでeditor動作しない…  
-> pyscriptapps.comで代用
## ファィル
・ pys_fetch_yaml.html -> 追加とかなし  
・ pys_fetch_yamlp.html -> 追加でpandasインポート  
・ pys_fetch_yaml_e.html -> py_editorで実行  
・ pys_fetch_yaml_ep.html -> py_editorで実行 追加でpandasインポート  
    pandasはインポートだけで処理は無し  
以下は同時に開いて速度比較用  
・ vsplit.html -> pyscripot 4種比較※[pyscriptapps.com](https://oxxpeh.pyscriptapps.com/pys-hikaku/latest/vsplit.html)で動作    
・ vsplit2.html -> pyscript使用(editorなし)とjavascriptのみ  
  [Githubpages](https://oxxpeh.pyscriptapps.com/pys-hikaku/latest/vsplit2.html)と[pyscriptapps.com](https://oxxpeh.pyscriptapps.com/pys-hikaku/latest/vsplit2.html)で動作  
・ pys_hikaku.jpg -> 4種比較の結果画面    
・ [pys_hikau.mp4](./pys_hikaku.mp4)  -> 4種比較の動作動画 (160kB)  
  
・editor.mp4 -> editorページの動作画面
## 参考サイト
<span style="color: #38761d;"><br>(参)<br>Using Panel in Pyodide & PyScript — Panel v1.6.2<br>https://panel.holoviz.org/how_to/wasm/standalone.html</span><br>
<span style="color: #38761d;"><br>(参)<br>Python editor - PyScript<br>https://docs.pyscript.net/2025.3.1/user-guide/editor/</span><br>
## その他
・結果画面とか  
![4種比較の結果](./pys_hikaku.jpg) 
・エディタページを作ってみたのでその動作画面
<video controls=controls autoplay loop muted width="800" height="450" >
<source src="https://raw.githubusercontent.com/oxxpeh/oxxpeh.github.io/main/2025/04_pyscript_editor/editor.mp4" type="video/mp4" />
</video>  
以下のことができる予定。(デザインセンスは無いので…)</p>
<ol>
<li>各セル(？)の入力出力のクリップボードへのコピー</li>
<li>各セル(？)の入力出力のクリア</li>
<li>各セルの実行</li>
<li>ネットからのソースの取得と下のセルに入力</li>
</ol><br />
・エディタでの自動実行<br />
エディタとは別でPyscript実行し、エディタ右下の実行アイコンクリックさせる<br />  
<pre><code>
import pyscript as ii_pys
ii_pys.document.getElementsByClassName('absolute py-editor-run-button')[0].click()
</code></pre><br />
・Editorの出力とかその他追記予定…  <br />
