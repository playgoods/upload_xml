from app import app
from flask_wtf.file import FileField
import os
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField, ValidationError


class UploadForm(FlaskForm):
    xml_file = FileField('Xml File')
    submit = SubmitField('Submit')

    def validate_xml_file(self, field):
        if field.data.filename[-4:].lower() != '.xml':
            raise ValidationError('Invalid file extension')


@app.route('/', methods=['GET', 'POST'])
def index():
    xml_upload = None
    form = UploadForm()
    if form.validate_on_submit():
        xml_upload = 'uploads/' + form.xml_file.data.filename
        form.xml_file.data.save(os.path.join(app.static_folder, xml_upload))
    return render_template('index.html', form=form, xml_upload=xml_upload)
