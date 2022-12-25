name = "Ryan"
def go_notgo(name):
    name_example = "James"
    if len(name) <= len(name_example):
        return("Так уж и быть можеш дружить с {0}".format(name))
    elif len(name) > len(name_example):
        return f"Я бы не стал дружить с {name}"
go_notgo(name)