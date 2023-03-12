from app import app, db
# from app.models.models import Item, Brand

@app.route("/")
def index():
    return "sem"

# @app.shell_context_processor
# def make_shell_context():
#     return dict(db=db, Item=Item)
