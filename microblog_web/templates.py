import datetime

from bottle import template


def _convert(message):
    message_id, datestamp, subject, body = message
    return {'subject':subject,'body':body.strip(), 'message_id': message_id,
            'date':datetime.datetime.fromtimestamp(datestamp)}

def render_root(messages):
    return template(root, {'messages': map(_convert, messages)})

def render_post(message):
    return template(post, _convert(message))

post = '''<html>
<head>
</head>
<body>
  <h1>{{subject}}</h1>
  <time datetime="{{date.isoformat()}}">{{date.strftime('%A, %B %d at %H:%M UTC')}}</time>
  <p>{{body}}</p>
</body>
</html>
'''

root = '''<html>
<h1>_</h1>
% for message in messages:
  <h2><a href="/{{message['message_id']}}">{{message['subject']}}</a></h2>
  <time datetime="{{message['date'].isoformat()}}">{{message['date'].strftime('%A, %B %d at %H:%M UTC')}}</time>
  <p>{{message['body']}}</p>
% end
</html>
'''
