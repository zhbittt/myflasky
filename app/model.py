from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, UniqueConstraint, Index
from sqlalchemy.orm import relationship
Base = declarative_base()

#=================================设计权限表================================
class Menu(Base):
    '''
    菜单组
    '''
    __tablename__ = "menu"
    id = Column(Integer,primary_key=True,autoincrement=True)
    title = Column(String(32),index=True)

    def __repr__(self):
        return '<Menu %r>'%self.title

class Group(Base):
    '''
    权限组
    '''
    __tablename__ = "group"

    id = Column(Integer,primary_key=True,autoincrement=True)
    caption = Column(String(32),index=True)
    menu_id = Column(Integer,ForeignKey("Menu.id"))

    # 方便以后查询，       正向    /反向查询
    menu = relationship("Menu",backref="group")

    def __repr__(self):
        return '<Group %r>'%self.caption

class Permission(Base):
    '''
    权限表
    '''
    __tablename__ = "permission"
    id = Column(Integer,primary_key=True,autoincrement=True)
    title = Column(String(32),index=True)    # 标题
    url = Column(String(64))      #含正则的url
    menu_gp = Column(String(32),nullable=True)  # 组内菜单
    code = Column(String(32))     #代码
    group_id = Column(Integer,ForeignKey("Group.id"))

    # 方便以后查询，       正向    /反向查询

    group = relationship("Group",backref='permission')

    def __repr__(self):
        return '<Permission %r>'%self.title

class User(Base):
    '''
    用户表
    '''
    __tablename__ = "user"
    id = Column(Integer,primary_key=True,autoincrement=True)
    username = Column(String(32))
    password = Column(String(32))
    email = Column(String(32))

    roles = relationship("Role",secondary='user2role', backref='user')

    def __repr__(self):
        return '<User %r>'%self.username

class Role(Base):
    '''
    角色表
    '''
    __tablename__ = "role"
    id = Column(Integer,primary_key=True,autoincrement=True)
    title = Column(String(32))

    permissions = relationship("Permission",secondary='role2permission', backref='role')

    def __repr__(self):
        return '<Role %r>'%self.title

class User2Role(Base):
    '''
    用户角色表
    '''

    __tablename__ = "user2role"
    id = Column(Integer,primary_key=True,autoincrement=True)
    user_id = Column(Integer,ForeignKey("User.id"))
    role_id = Column(Integer,ForeignKey("Role.id"))

    def __repr__(self):
        return '<User2Role %r-%r>'%(self.user_id.username,self.role_id.title)

class Role2Permission(Base):
    '''
    角色权限表
    '''

    __tablename__ = "role2permission"
    id = Column(Integer,primary_key=True,autoincrement=True)
    role_id = Column(Integer,ForeignKey("Role.id"))
    permission_id = Column(Integer,ForeignKey("Permission.id"))

    def __repr__(self):
        return '<Role2Permission %r-%r>'%(self.role_id.title,self.permission_id.title)


