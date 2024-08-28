# PowerShellでbeep音を鳴らす
テキスト入力ツール「ペースター」を使用してます。  
複数の条件の置換をしたくてPowerShellのreplaceを使用してましたが  
実行後音もならず寂しく思ったので追加を
## 使い方
「cv-html-s.vbs」と「cv-html-s.ps1」を作成
「cv-html-s.ps1」
```
$aa_cl =Get-Clipboard 
$aa_out = $aa_cl.Replace('(', '&#40;').Replace(')', '&#41;')
$aa_out = $aa_out.Replace('[', '&#91;').Replace(']', '&#93;')
$aa_out = $aa_out.Replace('<', '&lt;').Replace('>', '&gt;')
$aa_out = $aa_out.Replace('{', '&#123;').Replace('}', '&#125;')
$aa_out = $aa_out.Replace('/', '&#47;').Replace('\', '&#92;')
$aa_out = $aa_out.Replace('-', '&#8722;').Replace('=', '&#61;')
$aa_out = $aa_out.Replace(',', '&#44;').Replace('.', '&#46;')
$aa_out = $aa_out.Replace('|', '&#124;'.Replace(' ', '&nbsp;'))
set-Clipboard $aa_out

$source_beep = @"
using System;
using System.Runtime.InteropServices;

public static class WinApi
{
    [DllImport("kernel32.dll")]
    public static extern bool Beep(int freq,int duration);
}
"@
Add-Type -TypeDefinition $source_beep
 [WinApi]::Beep(440, 200)
```
「cv-html-s.vbs」
```
Option Explicit

' 本ファイルと同じディレクトリにある「同じファイル名.ps1」を、ウィンドウを開かずサイレント実行する
' (参)https://neos21.net/blog/2021/08/10-01.html
'Dim psFilePath : psFilePath = Replace(WScript.ScriptFullName, ".vbs", ".ps1")
Dim pspt : pspt = Replace(WScript.ScriptFullName, ".vbs", ".ps1")
'msgbox pspt
'Dim psFilePath : psFilePath = "C:\Users\nyobita\grp-clp.ps1"
'WScript.CreateObject("WScript.Shell").Run "C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe -NoLogo -File " & Chr(34) & psFilePath & Chr(34), 0
WScript.CreateObject("WScript.Shell").Run "C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe -NoLogo -File " & Chr(34) & pspt & Chr(34), 0
```
「MenuItem.txt」に`html記号置換  (&q) 	|[!E "C:\Users\user\cv-html-s.vbs" ]`追加  
「C:\Users\user」に両ファイルを保存した例  
## 参考サイト
<span style="color: #38761d;"><br>(参)<br>PowerShellでBEEP音を鳴らす #PowerShell - Qiita<br>https://qiita.com/mima_ita/items/ac33542ae3f2fb5c8778</span><br>
<span style="color: #38761d;"><br />(参)<br />PowerShell のウィンドウを一切表示させずに実行する - Neo's World<br />https://neos21.net/blog/2021/08/10-01.html</span><br />
<span style="color: #38761d;"><br>(参)<br>ペースター<br>https://autumn-soft.github.io/paster.htm</span><br>
  

