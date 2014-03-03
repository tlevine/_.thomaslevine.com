from bottle import template

def render_post(message):
    datestamp, subject, body = message
    params = {'date':datetime.datetime.fromtimestamp(datestamp),'subject':subject,'body':body}
    return template(templates.post, params)

post = '''<html>
<head>
</head>
<body>
  <h1>{{subject}}</h1>
  <time datetime="{{date.isoformat()}}">{{date.strftime('%A, %B %d at %H:%m UTC')}}</time>
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
