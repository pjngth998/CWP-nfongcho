def find_the_redheads(dic: dict[str, str]):
    result = []
    for fn, hair in dic.items():
        if hair == "red":
            result.append(fn)
    return result

dupont_family = {
"florian": "red",
"marie": "blond",
"virginie": "brunette",
"david": "red",
"franck": "red"
}
print(find_the_redheads(dupont_family))