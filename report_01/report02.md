# シミュレーション理工学基礎論レポート1

<!-- ## 問題

## 問題を解くための基本事項

a. 計算対象となる現象と方程式の説明
b. 方程式から計算モデル & 計算式の導出過程の説明
c. 初期条件などの計算条件
d. プログラミングでの工夫

## 問題に対する結果および考察

a. 結果
b. 計算の妥当性の確認方法と確認結果
c. シミュレーション結果に対する考察 -->

<!-- ## 必修：問題8.2

## 選択：問題8.3 -->

## 問題を解くための基本事項

a. 計算対象となる現象の説明

レナード・ジョーンズ・ポテンシャルについて説明を行う。

中性で球状の微小粒子の間の力は分子間の距離 $R$ の関数であり、$R$ が小さいと強い斥力, $R$ が大きいと引力となる。このような分子間力のポテンシャルを、レナード・ジョーンズ・ポテンシャルという。

イギリスの物理化学者レナード・ジョーンズは次式で近似的に表した。

$$
U(R) = -\frac{C_m}{R^m} + \frac{C_n}{R^n}
$$

$C_m, C_n$ は定数。

これをレナード・ジョーンズの(m, n)ポテンシャルとよび、とくに(6, 12)ポテンシャルが使われ、 次式のように変換され利用される。

$$
U(R) = U_0 \left( \left( \frac{\sigma}{R} \right) ^2 -2 \left( \frac{\sigma}{R} \right) ^6 \right)
$$

c. 初期条件などの計算条件

それぞれの粒子の初期条件については、特に指定のない限りはテキスト・資料に掲示されている $DATA$ を利用した。

## 問題8.2

### a.

プログラムmdをpython3で実装した。作成したプログラムはテキストにあるものをPython3に移植したものであるが、本プログラムではウィンドウ関連のコードまでは移植していないため、粒子の軌跡は画像として保存するようにした。

実行結果は下記のようになった。

![問題8-2aの実行時情報](./8-2a/8-2a.gif)

ncumを1000

### b.

### c.