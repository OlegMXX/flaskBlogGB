import os

from blog.app import app
from blog.models.database import db
from blog.models import User

if __name__ == '__main__':
    init_db()
    crate_admin()
    crate_tags()
    app.run(
        host='0.0.0.0',
        debug=True,
    )


#commands

#@app.cli.command("init-db")
def init_db():
   """
   Run in your terminal:
   flask init-db
   """
   db.create_all()
   print("done!")


#@app.cli.command("create-admin")
def create_admin():

    """
    Run in your terminal:
    ➜ flask create-admin
    > created admin: <User #1 'admin'>
    """
    from blog.models import User

    admin = User(username="admin", is_staff=True)
    admin.password = os.environ.get("ADMIN_PASSWORD") or "adminpass"

    db.session.add(admin)
    db.session.commit()

    print("created admin:", admin)


#@app.cli.command("create-tags")
def create_tags():
    """
    Run in your terminal:
    ➜ flask create-tags
    """
    from blog.models import Tag
    for name in [
        "flask",
        "django",
        "python",
        "sqlalchemy",
        "news",
    ]:
        tag = Tag(name=name)
        db.session.add(tag)
    db.session.commit()
    print("created tags")
