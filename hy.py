dict_item = {"a":"car","b":"bike","c":"train"}
result = map(lambda i:(i[0]+"___",i[1]),dict_item.items())
print(list(result))
