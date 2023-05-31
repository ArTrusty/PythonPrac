def list_hobbies():
    return["painting ","writing ","reading "]
hobbies = list_hobbies()
selected_string = hobbies[2]
select_paint = hobbies[0]
select_writ = hobbies[1]
info = "is one of my hobbies"

def build_sentence(info):
    sentence = selected_string + info
    
print(selected_string + info)   
print(select_paint +info)
print(select_writ + info)

