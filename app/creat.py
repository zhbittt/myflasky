from app import create_app,db,model

# db.create_all(app = create_app())
app = create_app()

with app.app_context():
    u1 = model.User(username='学生1', password='123', email='asd@5.com')
    u2 = model.User(username='学生2', password='123', email='asd@6.com')
    u3 = model.User(username='学生3', password='123', email='asd@7.com')
    u4 = model.User(username='学生4', password='123', email='asd@8.com')

    db.session.add(u1)
    db.session.add(u2)
    db.session.add(u3)
    db.session.add(u4)

    db.session.commit()
# 相当于SQL操作INSERT INTO User VALUES(字段1='值1',字段2='值2')，并将该SQL语句赋值到一个对象上
# u1 = db.User(username='路飞',password='123',email='asd@15.com')
# u2 = db.User(username='索隆',password='123',email='asd@16.com')
# u3 = db.User(username='香吉士',password='123',email='asd@17.com')
# u4 = db.User(username='娜美',password='123',email='asd@18.com')
#

#将对于数据库的操作保存在缓存中，既然是保存到缓存中，那么该数据库语句还没有提交到数据库中
# db.session.add(u1)
# db.session.add(u2)
# db.session.add(u3)
# db.session.add(u4)

#commit()和数据库中的commit指令一样，将数据库操作提交到数据库中。
# db.session.commit()


# 查询所有用户信息，并输出结果

    for user in model.User.query.all():
        print(user.id, user.username,user.password, user.email)