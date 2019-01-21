import json

def get_json_data(str):
    Lookupword = str
    json_data = open("/Users/svvarik/Documents/Projects/12Hours/uofthacksbeta19/wasteWizardData.json").read()
    data = json.loads(json_data)
    wordstorank = []
    for i in range(len(data)):
        if Lookupword in data[i]["keywords"]:
            list = data[i]["keywords"].split(",")
            for ln in list:
                if Lookupword in ln:
                    wordstorank.append(((ln), data[i]["category"]))
    wordstorank.sort()
    print(wordstorank[0][1])
    return wordstorank[0][1]

if __name__ == '__main__':
    get_json_data("toilet paper")