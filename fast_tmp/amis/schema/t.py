from .crud import CRUD
from .list import List
from .widgets import Column

x = List(
    body=CRUD(api="https://houtai.baidu.com/api/sample", columns=[
        Column(name="id", label="ID"),
        Column(name="engine", label="Rendering engine"),
        Column(name="browser", label="Browser"),
        Column(name="platform", label="Platform(s)"),
        Column(name="version", label="Engine version"),
        Column(name="grade", label="CSS grade"),
    ])
)
print(x.dict())
print(x.json())