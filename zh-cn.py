s = input('字符串：')
l = input('左括号：')
r = input('右括号：')
mp = { # 这部分内容可以随自己所需要用到的字符集尽情添加
    # 括号
    '(': f'{l}敲 Shift+9 键{r}',
    ')': f'{l}敲 Shift+0 键{r}',
    '[': f'{l}敲 [ 键{r}',
    ']': f'{l}敲 ] 键{r}',
    '{': f'{l}敲 Shift+[ 键{r}',
    '}': f'{l}敲 Shift+] 键{r}',
    '<': f'{l}敲 Shift+, 键{r}',
    '>': f'{l}敲 Shift+. 键{r}',
    # 中文括号
    '（': f'{l}敲 Shift+9 键{r}',
    '）': f'{l}敲 Shift+0 键{r}',
    '【': f'{l}敲 [ 键{r}',
    '】': f'{l}敲 ] 键{r}',
    '《': f'{l}敲 Shift+, 键{r}',
    '》': f'{l}敲 Shift+. 键{r}',
    # 其他符号
    '+': f'{l}敲 Shift+= 键{r}',
    ',': f'{l}敲 , 键{r}',
    '.': f'{l}敲 . 键{r}',
    '=': f'{l}敲 = 键{r}',
    ' ': f'{l}敲空格键{r}',
    # 部分中文字符
    '敲': f'{l}敲 Q 键{r}{l}敲 I 键{r}{l}敲 A 键{r}{l}敲 O 键{r}',
    '键': f'{l}敲 J 键{r}{l}敲 I 键{r}{l}敲 A 键{r}{l}敲 N 键{r}',
    '空': f'{l}敲 K 键{r}{l}敲 O 键{r}{l}敲 N 键{r}{l}敲 G 键{r}',
    '格': f'{l}敲 G 键{r}{l}敲 E 键{r}',
    '发': f'{l}敲 F 键{r}{l}敲 A 键{r}',
    '送': f'{l}敲 S 键{r}{l}敲 O 键{r}{l}敲 N 键{r}{l}敲 G 键{r}',
}
# 小写字母
for i in range(0, 26):
    mp[chr(ord('a') + i)] = f'{l}敲 {chr(ord("a") + i)} 键{r}'
# 大写字母
for i in range(0, 26):
    mp[chr(ord('A') + i)] = f'{l}敲 {chr(ord("A") + i)} 键{r}'
# 数字
for i in range(0, 10):
    mp[str(i)] = f'{l}敲 {i} 键{r}'
ans = ''
for i in range(0, len(s)):
    ans += mp[s[i]] + s[i]
print(f'{ans}{l}发送{r}')
