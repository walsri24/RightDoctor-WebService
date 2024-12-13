delete_form_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Delete Person</title>
</head>
<body>
    <h1>Are you sure you want to delete this person?</h1>
    <p>Name: {{ person.get('name') }}</p>
    <p>Age: {{ person.get('age') }}</p>
    <p>Gender: {{ person.get('gender') }}</p>
    <p>Mobile: {{ person.get('mobile') }}</p>
    <form method="POST" action="{{ action_url }}">
        <button type="submit">Delete</button>
    </form>
</body>
</html>
"""
