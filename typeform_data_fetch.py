import json
import requests
from typing import List, Dict, Any
import pandas as pd
from datetime import datetime

def list_workspace_forms(workspace_id, token: str):
    header = {"Authorization": "Bearer {}".format(token)}
    workspace_json = requests.get(
        f"https://api.typeform.com/forms?workspace_id={workspace_id}",
        params={"page": 1, "page_size": 200},
        headers=header,
    )
    form_list = workspace_json.json()["items"]
    return [{"id": form["id"], "title": form["title"]} for form in form_list]
# token = generated token place here!

# workspace_id = "9uPaNw"
forms = list_workspace_forms(workspace_id, token)
print(forms)
