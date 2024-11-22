from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,PasswordField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditorField


# WTForm for creating a blog post
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


# TODO: Create a RegisterForm to register new users
class Registration_form(FlaskForm):
    email = StringField(label="Email",validators=[DataRequired()])
    password = PasswordField(label="Password",validators=[DataRequired()])
    name = StringField(label="Name",validators=[DataRequired()])
    sign_up = SubmitField(label="Sign Me Up!")

# TODO: Create a LoginForm to login existing users
class Login_form(FlaskForm):
    email = StringField(label="Email", validators=[DataRequired()])
    password = PasswordField(label="Password", validators=[DataRequired()])
    login = SubmitField(label="Let Me In!")

# TODO: Create a CommentForm so users can leave comments below posts
class Comment_form(FlaskForm):
    comment = CKEditorField(label="comment",validators=[DataRequired()])
    submit = SubmitField("Submit Comment")