import re
# 四十五、正则基础

# 1、正则表达式
    # 记录文本规则的代码，需要导入re模块
    # 步骤：
    #     1、导入re模块
    #     2、使用match方法匹配，re.match()匹配，从起始位置开始，没匹配上就返回None
    #     3、匹配上就使用，group()提取数据
# 2、匹配单个字符
    # 1、. 匹配任意一个字符，除\n以外 --常用
res = re.match('.e','hello')     # res.group() = he
    # 2、[]匹配[]中列举的字符       --常用
res = re.match('[he]','hello') #h
res = re.match('[he]','ello') #e
res = re.match('[he][he]','hello') #he
res = re.match('[he].','hello') #he
res = re.match('[1-5]','25367') #1-5 = 12345
res = re.match('[a-zA-Z]','zxw') #z
# \d 匹配0-9
# \D 匹配
# \s 匹配空白 即空格或tab键   \s\s 一个tab
# \S 匹配非空白
# \w 匹配单词字符，即a-z,A-Z,0-9._,汉字   --常用
# \W 匹配非单词字符，
# 3、匹配多个字符
    # 1、* 匹配前一个字符出现0次或者无限次，即可有可无    --常用
res = re.match('\w*','zxw') # zxw
print(res.group())
    # 2、+ 匹配前一个字符出现1次或者无限次，即至少一次    --常用
    # 3、？匹配去啊一个字符出现1次或者0次               --常用
    # 4、{m} 匹配前一个字符出现m次
    # 5、{m,n} 匹配前一个字符出现从m次到n次 m<n
# 4、匹配开头结尾
    # ^ 匹配字符串开头 再[]表示不匹配，[^XX]表示出了xx的字符
    # $ 匹配字符串结尾

# 四十六、正则进阶

# 1、匹配分组
    # 1、｜ 匹配左右任意一个表达式
    # 2、(ab) 将括号中字符作为一个分组
res = re.match('\w@(163|qq|126).com','11@163.com')
    # 3、\num 引用分组num匹配到的字符串     经常在匹配标签的时候被使用
res = re.match(r'<(\w*)><(\w*)>.*</\2></\1>','<html><body>login</body></html>') # 从外到内，编号从1开始
print(res.group())
    # 4、（?P<name>）分组起别名
    # 5、（?P=name）引用别名为name分组匹配到的字符串
res = re.match(r'<(?P<l1>\w*)><(?P<l2>\w*)>.*</(?P=l2)></(?P=l1)>','<html><body>login</body></html>')
print(res.group())
# 2、高级用法
    # search():扫描整个字符串并返回第一个成功匹配的对象，如果匹配失败，则返回None
wm = re.search('re','jskjhressre') # re
print(type(wm))
    # findall():以列表形式返回整个字符串中所有匹配到的字符串
wm = re.findall('re','jskjhressre') # ['re','re'] 不需要用group提取
print(wm)
    # sub():将匹配到的数据进行替换
wm = re.sub('l','L','wwmmlaoliu',1) # 参数：旧内容，新内容，待匹配的字符串，要替换的次数，默认全部替换
print(type(wm))
print(wm)
    # split():根据匹配进行切割字符串，并返回一个列表
wm = re.split('|','hello,Python',3) #['', 'h', 'e', 'llo,Python'] 参数： 正则表达式、字符串、最大分割次数
print(wm)
# 3、贪婪与非贪婪
    # 贪婪匹配(默认):在满足匹配时，匹配尽可能长的字符串
    # 非贪婪：再满足匹配时，匹配尽可能短的字符串，使用?来表示非贪婪匹配
wm = re.match('em*','emmmmmmmm.....')   # emmmmmmmm 默认 贪婪
wm = re.match('em*?','emmmmmmmm.....')  # e 非贪婪

# 4、原生字符串
    # Python字符串前面加上r表示原生字符串
wm = print('six\\\told')
wm = print('six\told')
wm = re.match('\\\\','\gaame')
print(wm.group())   # 正则表达式中，匹配字符串中的字符\需要四个\,假如原生字符串，\\代表\