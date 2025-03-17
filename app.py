import chainlit as cl
import ollama

# Function to generate pickup line using LLaMA3.1 via Ollama
def generate_pickup_line(profile_text):
    response = ollama.chat(model="llama3.1", messages=[{"role": "user", "content": f"Create a pickup line based on the following Facebook profile: {profile_text}"}])
    
    # Safely extract content from the response
    if "message" in response and "content" in response["message"]:
        return response["message"]["content"].strip()
    else:
        return "Sorry, could not generate a pickup line."

# Chainlit app logic
@cl.on_message
async def handle_message(message: cl.Message):
    # Get the content of the profile from the message object
    profile_text = message.content
    
    # Generate the pickup line
    pickup_line = generate_pickup_line(profile_text)
    
    # Send the result back to the user
    await cl.Message(content=f"Profile: {profile_text}\nPickup Line: {pickup_line}").send()

# Entry point to run the Chainlit app
if __name__ == "__main__":
    cl.run()
