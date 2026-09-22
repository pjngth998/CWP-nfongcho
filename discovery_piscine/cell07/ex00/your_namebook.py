def array_of_names(dic: dict[str, str]):
    result = []
    for fn, ln in dic.items():
        fullname = fn[:1].upper() + fn[1:] + " " + ln[:1].upper() + ln[1:]
        result.append(fullname)
    return result

persons = {
"jean": "valjean",
"grace": "hopper",
"xavier": "niel",
"fifi": "brindacier"
}
print(array_of_names(persons))

