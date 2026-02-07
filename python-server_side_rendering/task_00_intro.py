import os

def generate_invitations(template, attendees):
    # Validation for input types
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return
    if not isinstance(attendees, list) or not all(isinstance(item, dict) for item in attendees):
        print("Error: Attendees must be a list of dictionaries.")
        return

    # Check for empty inputs
    if not template.strip():
        print("Template is empty, no output files generated.")
        return
    if not attendees:
        print("No attendees provided, no output files generated.")
        return

    # Process each attendee
    for i, attendee in enumerate(attendees, start=1):
        # We use a copy of the attendee dict to prepare the format data
        # We need to handle: 1. Missing keys, 2. None values
        
        # Define the keys we expect to see
        expected_keys = ["name", "event", "date", "location"]
        format_data = {}

        for key in expected_keys:
            val = attendee.get(key)
            # If value is None or empty string, use "N/A"
            if val is None or val == "":
                format_data[key] = "N/A"
            else:
                format_data[key] = val

        try:
            # Generate content using the prepared data
            output_content = template.format(**format_data)
            
            # Define filename
            filename = f"output_{i}.txt"
            
            # Write to file
            with open(filename, 'w') as f:
                f.write(output_content)
        
        except Exception as e:
            print(f"Error processing attendee {i}: {e}")