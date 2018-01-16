from flask import  request, render_template, session, redirect
from . import main
from ..pager import Pagination
from ..model import User

@main.before_request
def process_request1():
    if session.get("user_info") is None and request.path != '/login':
        return redirect('/login')

@main.after_request
def process_response1(response):
    return response


@main.route('/list',methods=['GET',])
def list():

    context= User.query.all()
    for user in context:
        print(user.id, user.username, user.password, user.email)

    # context=["a","b","c","d","e","f","g","h","i"]
    pager_obj = Pagination(len(context),request.path,per_page_count=5)
    context_list = context[pager_obj.start:pager_obj.end]
    page_html_list = pager_obj.page_html()
    return render_template('list_view.html',context_list=context_list,page_html_list=page_html_list)



@main.route('/login',methods=['GET','POST'])
def login():
    msg=""
    if request.method =='GET':
        return render_template('login.html',msg=msg)
    else:
        username = request.form.get("username")
        password = request.form.get("password")

        if username == 'asd' and password == "123":
            session["user_info"] = username
            return redirect('/list')
        else:
            msg ='用户名或密码错误'
            return render_template('login.html',msg=msg)


