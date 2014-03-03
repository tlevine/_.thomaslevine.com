post = '''<html>
<head>
</head>
<body>
  <h1>{{subject}}</h1>
  <time datetime="{{datetime.isoformat()}}">
  <p>{{body}}</p>
</body>
</html>
'''

root = '''<html>
    {{datestamp}}
    {{subject}}
    {{body}}
</html>
'''
