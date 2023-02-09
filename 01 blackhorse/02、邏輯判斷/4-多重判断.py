age = int(input('请问您的年龄是： \n'))

if age < 18:
    print(f'您才{age}歲，與工作年龄不符，请回吧')
# elif(else if 的縮寫)
# elif (age >= 18) and (age < 60):
elif 18<=age<=60:
    print(f'噢哟，才{age}歲！我们公司最希望有这么新鲜的肝啦！')
else:
    print(f'姥爷，您都{age}歲了。该退休了，別內卷了')
