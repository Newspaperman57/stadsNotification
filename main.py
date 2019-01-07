import sys
import json
import requests
from datetime import datetime
from requests_html import HTMLSession

session = HTMLSession()
# Get cookies
session.get("https://sb.aau.dk/sb-ad/sb/index.jsp")
# Login
session.post("https://sb.aau.dk/sb-ad/sb/index.jsp", headers={"Content-Type":"application/x-www-form-urlencoded"}, data="brugernavn=" + sys.argv[1] + "&adgangskode=" + sys.argv[2] + "&submit_action=login")
# Get grades
gradesHTML = session.get("https://sb.aau.dk/sb-ad/sb/resultater/studresultater.jsp").html
grades = []
for grade in gradesHTML.find("TR.DataSelect"):
    gradeJson = grade.text.split("\n")
    grades.append({
        "name": gradeJson[0],
        "date": datetime.strptime(gradeJson[1], "%d.%m.%Y").isoformat(),
        "gradeNumber": gradeJson[2],
        "gradeLetter": gradeJson[3] if gradeJson[2].isdigit() else None,
        "ECTS": gradeJson[4] if gradeJson[2].isdigit() else gradeJson[3]
    })
print(json.dumps(grades))
