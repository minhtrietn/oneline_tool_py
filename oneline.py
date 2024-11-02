txt = open("Your-file").read()

print(f"""exec("{repr(txt).replace("'", "")}")""")
