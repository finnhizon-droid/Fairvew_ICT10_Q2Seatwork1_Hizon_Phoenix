from pyscript import document



#List of the already accepted basketball varsity members

varsity_members = ["Phoenix Hizon", "Erin Urbano", "Joaquin Castor", "Jarvis Joven", "Enzo Ruiz", "Rocky Saludez", "Miguel Santos"]

#Clicking the button triggers this event to verify if the inputted name is in the given list

def verify(event):

#Getting the values of the input elements

    first_name = document.getElementById("first_name").value.strip()
    last_name = document.getElementById("last_name").value.strip()

    inputted_name = first_name + " " + last_name

#Verify membership using "in"

    real = inputted_name in varsity_members

#Output messages gets determined by the boolean index (False = 0, True = 1)

    output_messages = [
        "Sorry " + inputted_name + ", your name is not on the roster.",
        "Congratulations " + inputted_name + "! You are now officially on the roster."
    ]

#CSS

    style_classes = ["member-not-found", "member-found"]

#Determine the text to be shown for both true and false

    result_div = document.getElementById("result")
    result_div.innerText = output_messages[real]
    
    result_div.className = ""
    result_div.classList.add(style_classes[real])
    result_div.style.opacity = "1"