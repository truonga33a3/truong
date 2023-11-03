from main import db, app
from models import Priority, Status

app.app_context().push()

# add Priority
p = Priority(text ='Priority 1')
db.session.add(p)
db.session.commit()
p = Priority(text ='Priority 2')
db.session.add(p)
db.session.commit()
p = Priority(text ='Priority 3')
db.session.add(p)
db.session.commit()
p = Priority(text ='Priority 4')
db.session.add(p)
db.session.commit()



# add giá trị Status
ds = Status(description = 'Chưa thực hiện')
db.session.add(ds)
db.session.commit()
ds = Status(description = 'Đang thực hiện')
db.session.add(ds)
db.session.commit()
ds = Status(description = 'Quá hạn')
db.session.add(ds)
db.session.commit()
ds = Status(description = 'Hoàn thành')
db.session.add(ds)
db.session.commit()

