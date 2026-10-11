from pyscript import document


# List of the already accepted basketball varsity members
varsity_members = [
    "Phoenix Hizon",
    "Erin Urbano",
    "Joaquin Castor",
    "Jarvis Joven",
    "Enzo Ruiz",
    "Rocky Saludez",
    "Miguel Santos",
]


# Clicking the button triggers this event to verify if the inputted name is in the given list
def verify(event):
    
# Get input values and combine into one full name using f-strings

    first_name = document.getElementById("first_name").value.strip()
    last_name = document.getElementById("last_name").value.strip()
    
    candidate_name = f"{first_name} {last_name}"

# Using if/else statements to verify the inputted name and set the message
    
    if candidate_name in varsity_members:
        message = f"Congratulations {candidate_name}! You are now part of the ICT club."
        styling = "member-found"
        
    else:
        message = f"Sorry {candidate_name}, your name is not on the list."
        styling = "member-not-found"

# Display the text and apply CSS to it
    
    result_div = document.getElementById("result")
    result_div.innerText = message
    result_div.className = styling
    result_div.style.opacity = "1"
