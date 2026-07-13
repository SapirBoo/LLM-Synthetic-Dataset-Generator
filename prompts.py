def  build_user_prompt(topic,studio_style,studio_type,num_of_rows,additional_requirements=None):

  return f"""Generate a synthetic dataset for a {studio_style} {studio_type}.

The name of studio is {topic}

Generate exactly {num_of_rows} objects.

  Include:

  - Class Name
  - Instructor
  - Day
  - Time
  - Duration
  - Capacity
  - Equipment
  - Membership Type
  - Price


Additional requirements:
{additional_requirements}

Make the data realistic.
Every object must contain exactly these fields:
Class Name,
Instructor,
Day,
Time,
Duration,
Capacity,
Equipment,
Membership Type,
Price.

Never omit fields.

Return a JSON array only.

Example:
[
  {{
   "Class Name": "Yoga Flow",
   "Instructor": "Anna",
   "Day": "Monday",
   "Time": "18:00",
   "Duration": "60 minutes",
   "Capacity": 12,
   "Equipment": "Yoga Mat",
   "Membership Type": "Premium",
   "Price": 25
 }}
]

Do not explain anything.

Do not include reasoning.

Do not include <think> tags.

Do not include markdown.

The first character must be '['."""
