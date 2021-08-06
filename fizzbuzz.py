combos = {
3: "Fizz",
5: "Buzz",
7: "Carot"
}

output = ""
for i in range(100+1):
    for special in combos:
        if i % special == 0:
            output += combos[special]
    
    if output == "":
        output += str(i)
     
    print(output)
    output = ""
