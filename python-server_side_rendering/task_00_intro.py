import os

def generate_invitations(template, attendees):
    # Data validation
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return
    if not isinstance(attendees, list) or not all(isinstance(item, dict) for item in attendees):
        print("Error: Attendees must be a list of dictionaries.")
        return

    # Check for empty inputs
    if not template:
        print("Template is empty, no output files generated.")
        return
    if not attendees:
        print("No attendees provided, no output files generated.")
        return

    # Process attendees
    for i, attendee in enumerate(attendees, start=1):
        # Create a copy to avoid modifying the original data
        # Fill missing or None values with "N/A"
        data = {k: (v if v is not None else "N/A") for k, v in attendee.items()}
        
        # Ensure standard keys exist even if not in the dictionary at all
        for key in ["name", "event", "date", "location"]:
            if key not in data or data[key] == "":
                data[key] = "N/A"

        try:
            # Use format(**data) to map keys to {placeholders}
            processed_content = template.format(**data)
            
            filename = f"output_{i}.txt"
            
            # Write file (if it exists, it will be overwritten)
            with open(filename, 'w') as f:
                f.write(processed_content)
                
        except KeyError as e:
            print(f"Error: Template contains a placeholder {e} not provided in data.")
        except Exception as e:
            print(f"Error: {e}")