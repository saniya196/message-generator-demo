templates = {
    "diwali": "Hello {name}, Diwali greetings! We wish you the best holiday. Namaste!",
    "new year": "Happy New Year {name}! Wishing you success and happiness in the coming year.",
    "birthday": "Hello {name}, wishing you a wonderful birthday filled with joy and smiles!",
}

def generate_message(prompt, name="Customer"):
    prompt = prompt.lower()
    for key, template in templates.items():
        if key in prompt:
            return template.format(name=name)
    return f"Hello {name}, best wishes!"

if __name__ == "__main__":
    prompt = input("Enter prompt: ")
    name = input("Enter name (optional): ") or "Customer"
    print("\nGenerated Message:\n")
    print(generate_message(prompt, name))
