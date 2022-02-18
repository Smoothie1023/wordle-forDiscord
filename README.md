# wordle-forDiscord
WordleをDiscordで遊べるBotです．

# Requirements
pycord

python3

wordlist.txt(５文字の英単語を改行で区切って入力されたテキストファイル）

guild_id.txt(Botを動作させるサーバーのIDをここに）Atomを使用しているため１行目が改行されている必要があります．

token.txt(Botのトークンをここに）注意点は上に同じ

# Usage
/startコマンドを使うとwordlist.txt中の5文字の英単語がランダムに選ばれ初期化処理を行います．

その後/answer [ans]コマンドでans部分に5文字の英単語を入力しコマンドを使います.

/startコマンドで選ばれた単語と比較され位置と文字があっていれば緑，文字だけ合っていれば赤で結果をBotが返答します．

/killコマンドで/startコマンドが実行されていればゲームの中断を行えます．（今後のアップデートでコマンドを実行したユーザーのみ解答できるようにする可能性があるため実装しました．）

ルールは本家と同じです．

# Note
pycordを用いていますので，環境構築の際には注意してください．

discord.pyとはプログラムの書き方が異なっているはずです．

# Author
Smoothie

# License
The source code is licensed MIT
