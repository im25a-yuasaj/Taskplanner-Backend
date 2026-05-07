from models.user import User
from models.category import Category
from models.material import Material
from models.priority import Priority
from models.progress import Progress
from models.task import Task
from datetime import datetime

def test_user_model_creation(db_session):
    new_user = User(BenutzerName="testuser", BenutzerPWD="testpassword")
    db_session.add(new_user)
    db_session.commit()
    
    retrieved_user = db_session.query(User).filter_by(BenutzerName="testuser").first()
    assert retrieved_user is not None
    assert retrieved_user.BenutzerName == "testuser"
    assert retrieved_user.BenutzerPWD == "testpassword"
    assert retrieved_user.BenutzerID is not None

def test_user_repr():
    user = User(BenutzerName="johndoe")
    assert repr(user) == "<Benutzer johndoe>"

def test_category_pydantic():
    cat = Category(CategoryID=1, Category="Work", IsActive=True)
    assert cat.Category == "Work"
    assert cat.IsActive is True

def test_material_pydantic():
    mat = Material(MaterialID=1, Material="Hammer", IsActive=True)
    assert mat.Material == "Hammer"

def test_priority_pydantic():
    prio = Priority(PriorityID=1, Priority="High")
    assert prio.Priority == "High"

def test_progress_pydantic():
    prog = Progress(ProgressID=1, Progress="In Progress")
    assert prog.Progress == "In Progress"

def test_task_pydantic():
    task = Task(
        taskID=1,
        title="Fix bug",
        start=datetime.now(),
        end=datetime.now(),
        location="Office",
        coordinates="0,0",
        note="ASAP",
        categoryID="1",
        priorityID=1,
        progressID=1,
        userID=1
    )
    assert task.title == "Fix bug"
