def get_product(**data): # Needs ** to get any kind of data, when called it needs the name of the param and returns JSON.
    print(data["name"])
    print(data)
    
get_product(id="5", name="iPhone", desc="iPhone 15 Pro")