from flask import Blueprint, request
from backend.models import User, EntryReport
import json
from backend import db

events = Blueprint('events', __name__)


@events.route('/events/create', methods=['POST', 'GET'])
def new_event():
    request_json = request.get_json()
    auth_token = request_json['auth_token']
    user = User.verify_auth_token(auth_token)
    if not user:
        return json.dumps({'status': 0})
    else:
        report = request_json['report']
        location = request_json['location']
        event = EntryReport(reporter_id=user.id, report=report, location=location)
        db.session.add(event)
        db.session.commit()
        return json.dumps({'status': 1})
