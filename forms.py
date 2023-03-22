from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL, Email, InputRequired, Length
from flask_ckeditor import CKEditorField

##WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


class RegisterForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired(), InputRequired()])
    email = StringField("Email", validators=[DataRequired(), InputRequired(), Email(check_deliverability=True)])
    password = PasswordField("Password", validators=[DataRequired(), InputRequired(), Length(min=8, max=-1)])
    submit = SubmitField("SING ME UP")


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), InputRequired(), Email(check_deliverability=True)])
    password = PasswordField("Password", validators=[DataRequired(), InputRequired()])
    submit = SubmitField("LET ME IN")


class CommentForm(FlaskForm):
    comment_text = CKEditorField("Comment", validators=[DataRequired()])
    submit = SubmitField("SUBMIT COMMENT")
