import os

def generate_invitations(template, attendees):
    # Check if template is a string
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return

    # Check if attendees is a list of dictionaries
    if not isinstance(attendees, list) or not all(isinstance(item, dict) for item in attendees):
        print("Error: Attendees must be a list of dictionaries.")
        return

    # Check for empty input
    if not template:
        print("Template is empty, no output files generated.")
        return
    if not attendees:
        print("No attendees provided, no output files generated.")
        return

    # Process each attendee
    for i, attendee in enumerate(attendees, start=1):
        # Handle missing keys by using .get() with "N/A" as default
        processed_template = template.format(
            name=attendee.get("name") if attendee.get("name") else "N/A",
            event_title=attendee.get("event_title") if attendee.get("event_title") else "N/A",
            event_date=attendee.get("event_date") if attendee.get("event_date") else "N/A",
            event_location=attendee.get("event_location") if attendee.get("event_location") else "N/A"
        )

        # Write to file
        template = f"output_{i}.txt"
        try:
            with open(template, 'w') as f:
                f.write(processed_template)
        except Exception as e:
            print(f"Error writing to {template}: {e}")