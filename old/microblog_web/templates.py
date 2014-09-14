import datetime

from bottle import template

def _convert(message):
    message_id, datestamp, subject, body = message
    return {'subject':subject,'body':body.strip(), 'message_id': message_id,
            'date':datetime.datetime.fromtimestamp(datestamp)}

def render_root(messages):
    return template(_base % _root, {'messages': map(_convert, messages)})

def render_post(message):
    return template(_base % _post, _convert(message))

_post = '''
  <h1>{{subject}}</h1>
  <time datetime="{{date.isoformat()}}">{{date.strftime('%A, %B %d at %H:%M UTC')}}</time>
  <p>{{body}}</p>
'''

_root = '''
<h1>_</h1>
% for message in messages:
  <h2><a href="/{{message['message_id']}}">{{message['subject']}}</a></h2>
  <time datetime="{{message['date'].isoformat()}}">{{message['date'].strftime('%A, %B %d at %H:%M UTC')}}</time>
  <p>{{message['body']}}</p>
% end
'''

_base = '''<!DOCTYPE html>
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
  <meta charset="utf-8">
  <title>Thomas Levine, Dada Artist</title>
  <meta content="" name="description">
  <meta content="Thomas Levine" name="author">
  <link href='http://fonts.googleapis.com/css?family=Open+Sans:400italic,400,700' rel='stylesheet' type='text/css'>
  <script src='https://c328740.ssl.cf1.rackcdn.com/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML' type='text/javascript'></script>
  <link href='http://thomaslevine.com/css/style-cb653401acb.css' rel='stylesheet'>
</head>
<body>
  <div id="wrapper">
    <div id="container">
      <div id='article-wrapper'>
        <article>
          <header>
            %s
          </header>
        </article>
      </div>
    </div>
  </div>
</body>
</html>
'''
