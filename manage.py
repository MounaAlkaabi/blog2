import os
from flask.ext.script import Manager
from blog.database import session
from blog.model import Entry
from blog import app

manager = Manager(app)


@manager.command
def seed():
    content = ""
    for i in range(25):
        entry = Entry(
            title="Test Entry #{}".format(i),
            content=content
        )
        session.add(entry)
    session.commit()
    
@manager.command
def run():
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)

if __name__ == "__main__":
    manager.run()