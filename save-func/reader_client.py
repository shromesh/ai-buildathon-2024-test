import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account.
cred = credentials.Certificate(
    "/Users/ryoma/Downloads/ai-buildathon-test-nov9-1-3fac5865e2e6.json"
)

app = firebase_admin.initialize_app(cred)

db = firestore.client()


doc_ref = db.collection("data_collection")

print(dict(doc_ref))

## conda install auto::python-firebase
## 失敗。チャンネルが存在しないというエラー。
## 次を試す。
## /Users/ryoma/anaconda3/envs/firestore-test/bin/pip install firebase-admin
## import errorは解決。
## しかし、google.api_core.exceptions.PermissionDenied
