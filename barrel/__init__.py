# Package File
import flask

app = flask.Flask(__name__)   

#
## V1 API
#
api_base_prefix = "/api"
api_v1_prefix = api_base_prefix+"/v1"

@app.route(api_v1_prefix+'/project/byuid/<string:projectUID>')
def get_project_by_UID(projectUID):
    if len(projectUID) != 8:
        return {"error": "invalid length"}, 400 
    elif not projectUID.isalnum():
        return {"error": "invalid characters"}, 400
    
    # todo return project info
    return {
        "projectUID":projectUID,
        
        }



@app.route('/<path:path>')
def debugpath(path):
    return path
