person_form_template = """
<!DOCTYPE html>
<html>
<head>
    <title>{{ action }} Person</title>
</head>
<body>
    <h1>{{ action }} Person</h1>
    <form method="POST" action="{{ action_url }}">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" value="{{ person.get('name', '') }}" required><br><br>
        
        <label for="age">Age:</label>
        <input type="number" id="age" name="age" value="{{ person.get('age', '') }}" required><br><br>
        
        <label for="gender">Gender:</label>
        <select id="gender" name="gender" required>
            <option value="Male" {% if person.get('gender') == 'Male' %}selected{% endif %}>Male</option>
            <option value="Female" {% if person.get('gender') == 'Female' %}selected{% endif %}>Female</option>
            <option value="Other" {% if person.get('gender') == 'Other' %}selected{% endif %}>Other</option>
        </select><br><br>
        
        <label for="mobile">Mobile:</label>
        <input type="text" id="mobile" name="mobile" value="{{ person.get('mobile', '') }}" required><br><br>
        
        <button type="submit">{{ action }}</button>
    </form>
</body>
</html>
"""
