import ollama

# Function to read Facebook profiles from a txt file
def read_profiles(file_path):
    with open(file_path, "r") as file:
        profiles = file.readlines()
    return profiles

# Function to generate pickup line using LLaMA3.1 via Ollama
def generate_pickup_line(profile_text):
    response = ollama.chat(model="llama3.1", messages=[{"role": "user", "content": f"Create a pickup line based on the following Facebook profile: {profile_text}"}])
    
    # Print the entire response to inspect its structure (optional for debugging)
    print("Response from Ollama:", response)
    
    # Safely extract content from the response
    if "message" in response and "content" in response["message"]:
        return response["message"]["content"].strip()
    else:
        return "Sorry, could not generate a pickup line."

# Main function to process profiles and generate pickup lines
def process_profiles(file_path):
    profiles = read_profiles(file_path)  # Read profiles from the file
    
    for profile in profiles:
        profile = profile.strip()  # Clean any extra newlines or spaces
        pickup_line = generate_pickup_line(profile)
        print(f"Profile: {profile}\nPickup Line: {pickup_line}\n")

# Run the function with the provided profile file
if __name__ == "__main__":
    process_profiles("profiles.txt")  # Replace with your actual path to the profile file