def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return

    if not isinstance(attendees, list) or not all(
        isinstance(item, dict) for item in attendees
    ):
        print("Error: Attendees must be a list of dictionaries.")
        return

    if not template:
        print("Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return

    for index, attendee in enumerate(attendees, start=1):
        output = template

        output = output.replace(
            "{name}", attendee.get("name") or "N/A"
        )
        output = output.replace(
            "{event_title}", attendee.get("event_title") or "N/A"
        )
        output = output.replace(
            "{event_date}", attendee.get("event_date") or "N/A"
        )
        output = output.replace(
            "{event_location}", attendee.get("event_location") or "N/A"
        )

        with open(f"output_{index}.txt", "w") as file:
            file.write(output)
